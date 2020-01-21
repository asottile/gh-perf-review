[![Build Status](https://dev.azure.com/asottile/asottile/_apis/build/status/asottile.gh-perf-review?branchName=master)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=8&branchName=master)

gh-perf-review
==============

hackety tool to view github PRs for a period

## setting up a token

1. Create a gh token on [the settings tab](//github.com/settings/tokens/new)
    - use `repo` scope if you need private repos, otherwise `public_repo`
    - if your org is protected by SSO, make sure to enable that for the token by clicking the Authorize button within the Enable SSO dropdown
1. Write out the settings file needed for this script

    ```bash
    echo '{"token": "TOKEN HERE"}' > .github-auth.json
    chmod 600 .github-auth.json
    "${EDITOR:-vim}" .github-auth.json
    ```

## generating markdown output

Usage: `python3 gh_perf_review.py ORG YEAR PERIOD [--user USER] [--involves INVOLVES]`

- `ORG`: the github organization to search in
- `YEAR`: the four digit year to search in
- `PERIOD`: the time period to search in, currently supported: Q1, Q2, Q3, Q4,
  H1, H2, Y
- `--user USER`: optional, will use the authenticated user otherwise
- `--involves INVOLVES`: optional, will filter for reviews involving this reviewer

The script writes its output to stdout, if you'd like to capture that, redirect
it to a file:

```bash
python3 gh_perf_review.py pre-commit 2018 Q4 > report.md
```

If you'd like to convert it to html, one such tool is
[markdown-code-blocks](https://github.com/asottile/markdown-code-blocks).

```bash
python3 gh_perf_review.py pre-commit 2018 Q4 |
    markdown-code-blocks-highlight /dev/stdin |
    sed 's|<body>|<head><style>td, th { padding: 5px; border: 1px solid #000; }</style></head><body>|g' > report.htm
```

## sample output

[pre-commit 2018 Y](example.md)
