from __future__ import annotations

import argparse
import collections
import datetime
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any
from typing import Counter
from typing import DefaultDict
from typing import NamedTuple
from typing import Sequence

DATE_FMT = '%Y-%m-%dT%H:%M:%SZ'
PERIODS = {
    'q1': ('01-01', '03-31'),
    'q2': ('04-01', '06-30'),
    'q3': ('07-01', '09-30'),
    'q4': ('10-01', '12-31'),
    'h1': ('01-01', '06-30'),
    'h2': ('07-01', '12-31'),
    'y': ('01-01', '12-31'),
}


class Response(NamedTuple):
    json: Any
    links: dict[str, str]


class RepoCount(NamedTuple):
    repo: str
    prs: int

    @property
    def sort_key(self) -> tuple[int, str]:
        return -1 * self.prs, self.repo


class _PRDisplay(NamedTuple):
    date: str
    link: str
    title: str


class PR(NamedTuple):
    dt: datetime.datetime
    link_text: str
    link_url: str
    title: str

    @property
    def display(self) -> _PRDisplay:
        return _PRDisplay(
            self.dt.date().isoformat(),
            f'[{self.link_text}]',
            self.title,
        )

    @classmethod
    def from_gh(cls, dct: dict[str, Any]) -> PR:
        date = datetime.datetime.strptime(dct['closed_at'], DATE_FMT)
        _, _, repo = dct['repository_url'].rpartition('/')
        link_text = f"{repo}#{dct['number']}"
        return cls(date, link_text, dct['html_url'], dct['title'])


def _parse_link(lnk: str | None) -> dict[str, str]:
    if lnk is None:
        return {}

    ret = {}
    parts = lnk.split(',')
    for part in parts:
        link, _, rel = part.partition(';')
        link, rel = link.strip(), rel.strip()
        assert link.startswith('<') and link.endswith('>'), link
        assert rel.startswith('rel="') and rel.endswith('"'), rel
        link, rel = link[1:-1], rel[len('rel="'):-1]
        ret[rel] = link
    return ret


def _req(url: str, **kwargs: Any) -> Response:
    try:
        resp = urllib.request.urlopen(urllib.request.Request(url, **kwargs))
    except urllib.error.HTTPError as e:
        print(f'HTTPError {e.code} {e.reason}.')
        print(json.dumps(json.loads(e.read().decode()), indent=4))
        sys.exit(-1)

    return Response(json.load(resp), _parse_link(resp.headers['link']))


def _get_all(url: str, **kwargs: Any) -> list[dict[str, Any]]:
    ret: list[dict[str, Any]] = []
    while True:
        print('.', end='', file=sys.stderr, flush=True)
        resp, links = _req(url, **kwargs)
        ret.extend(resp['items'])
        if 'next' in links:
            time.sleep(1)
            url = links['next']
        else:
            print(file=sys.stderr, flush=True)
            return ret


def _md_table(items: Sequence[Any]) -> str:
    field_count = len(items[0])
    columns = items[0]._fields
    widths = [
        max(
            len(str(x))
            for x in [item[idx] for item in items] + [columns[idx]]
        )
        for idx in range(field_count)
    ]
    fmts = [
        '{{: {}{}}}'.format(
            '>' if isinstance(items[0][idx], (int, float)) else '<',
            widths[idx],
        )
        for idx in range(field_count)
    ]

    fmt = f"|{'|'.join(fmts)}|\n"
    header = fmt.format(*columns)
    sep = fmt.format(*('-' * width for width in widths))
    lines = [fmt.format(*(str(x) for x in item)) for item in items]
    return f"{header}{sep}{''.join(lines)}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('org')
    parser.add_argument('year', type=int)
    parser.add_argument('period', type=str.lower, choices=PERIODS)
    # TODO sanitize this somehow?
    parser.add_argument('--api-root', default='https://api.github.com')
    parser.add_argument('--user')
    parser.add_argument('--involves', type=str.lower)
    args = parser.parse_args()

    token = json.loads(open('.github-auth.json').read())['token']
    headers = {'Authorization': f'token {token}'}

    if args.user is None:
        user_resp, _ = _req(f'{args.api_root}/user', headers=headers)
        user = user_resp['login']
    else:
        user = args.user

    start, end = PERIODS[args.period]
    query = (
        f'org:{args.org} is:pr is:merged author:{user} '
        f'merged:{args.year}-{start}..{args.year}-{end}'
    )
    if args.involves:
        query = f'{query} involves:{args.involves}'

    query = urllib.parse.quote(query)
    url = f'{args.api_root}/search/issues?q={query}&per_page=100&sort=merged'
    resp = _get_all(url, headers=headers)

    by_repo: Counter[str] = collections.Counter()
    for pr_dct in resp:
        by_repo['/'.join(pr_dct['repository_url'].rsplit('/', 2)[-2:])] += 1

    prs = sorted(PR.from_gh(pr) for pr in resp)
    by_month: DefaultDict[int, list[PR]] = collections.defaultdict(list)
    for pr in prs:
        by_month[pr.dt.month].append(pr)

    print(f"# {user}'s {args.year} {args.period.upper()} summary ({args.org})")
    print()
    print(f'- **{len(resp)}** PRs')
    print(f'- **{len(by_repo)}** repos')
    print()
    print('## by repository')
    print()
    most_common = sorted(
        (RepoCount(*rc) for rc in by_repo.most_common()),
        key=lambda rc: rc.sort_key,
    )
    print(_md_table(most_common))
    print()
    print('## by date')
    print()

    for month_prs in by_month.values():
        print(
            f"### {month_prs[0].dt.strftime('%B').lower()} "
            f'({len(month_prs)} prs)',
        )
        print()
        print(_md_table([pr.display for pr in month_prs]))
        print()

    print()
    for pr in prs:
        print(f'[{pr.link_text}]: {pr.link_url}')

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
