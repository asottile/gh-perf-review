# asottile's 2018 Y summary (pre-commit)

- **165** PRs
- **21** repos

## by repository

|repo                               |prs|
|-----------------------------------|---|
|pre-commit/pre-commit              | 80|
|pre-commit/pre-commit-hooks        | 27|
|pre-commit/pre-commit.github.io    | 22|
|pre-commit/pre-commit-mirror-maker | 13|
|pre-commit/cron-mirror-creation    |  5|
|pre-commit/pygrep-hooks            |  2|
|pre-commit/pre-commit-docker-flake8|  2|
|pre-commit/pre-commit-installed    |  1|
|pre-commit/mirrors-yapf            |  1|
|pre-commit/mirrors-scss-lint       |  1|
|pre-commit/mirrors-ruby-lint       |  1|
|pre-commit/mirrors-pylint          |  1|
|pre-commit/mirrors-puppet-lint     |  1|
|pre-commit/mirrors-jshint          |  1|
|pre-commit/mirrors-fixmyjs         |  1|
|pre-commit/mirrors-eslint          |  1|
|pre-commit/mirrors-csslint         |  1|
|pre-commit/mirrors-coffeelint      |  1|
|pre-commit/mirrors-autopep8        |  1|
|pre-commit/mirrors-isort           |  1|
|pre-commit/demo-repo               |  1|


## by date

### january

|date      |link                        |title                                            |
|----------|----------------------------|-------------------------------------------------|
|2018-01-02|[pre-commit#673]            |Slower travis-ci workaround after 2017 q4 updates|
|2018-01-03|[pre-commit#674]            |Simplify cross version tests                     |
|2018-01-08|[pre-commit#676]            |Invoke `git diff` without a pager                |
|2018-01-09|[pre-commit#680]            |Fix broken local golang repos                    |
|2018-01-12|[pre-commit#684]            |Move PrefixedCommandRunner -> Prefix             |
|2018-01-13|[pre-commit#685]            |Support node on windows with long path hack      |
|2018-01-14|[pre-commit#686]            |Simplify prefix a bit                            |
|2018-01-14|[pre-commit#687]            |Deprecate the pcre language                      |
|2018-01-14|[pre-commit#688]            |https-ify links                                  |
|2018-01-14|[pre-commit.github.io#152]  |Mention node support on windows                  |
|2018-01-21|[pre-commit-mirror-maker#25]|Replace deprecated yield_fixture with fixture    |
|2018-01-22|[pre-commit#690]            |Replace deprecated yield_fixture with fixture    |
|2018-01-22|[pre-commit-hooks#259]      |Replace deprecated yield_fixture with fixture    |
|2018-01-30|[pre-commit#694]            |Fix legacy commit-msg hooks                      |


### february

|date      |link                      |title                                                  |
|----------|--------------------------|-------------------------------------------------------|
|2018-02-01|[pre-commit#698]          |Change ignored cache dir for pytest 3.4.0              |
|2018-02-01|[pre-commit-hooks#261]    |Change ignored cache dir for pytest 3.4.0              |
|2018-02-01|[pre-commit.github.io#153]|Document `py` launcher translation for windows         |
|2018-02-04|[pre-commit#699]          |Rewrite the hook template in python                    |
|2018-02-12|[pre-commit.github.io#156]|Add xcodeproj-sort-pre-commit-hook                     |
|2018-02-19|[pre-commit#700]          |Move pre_commit.schema to cfgv library                 |
|2018-02-19|[pre-commit-hooks#266]    |Fix no-commit-to-branch when not on a branch           |
|2018-02-24|[pre-commit#710]          |Don't modify user's npmrc under test                   |
|2018-02-24|[pre-commit#712]          |Don't write to the home directory under test           |
|2018-02-24|[pre-commit-hooks#269]    |Don't pass filenames for no-commit-to-branch           |
|2018-02-25|[pre-commit#711]          |Each set of additional dependencies gets its own env   |
|2018-02-25|[pre-commit#713]          |Allow autoupdate --repo to be specified multiple times |
|2018-02-25|[pre-commit#714]          |Move cwd() to tests-only                               |
|2018-02-26|[pre-commit#715]          |Migrate sha -> rev                                     |
|2018-02-28|[pre-commit-hooks#271]    |Don't add end-of-file newline while trimming whitespace|


### march

|date      |link                        |title                                      |
|----------|----------------------------|-------------------------------------------|
|2018-03-01|[pre-commit#717]            |Use --clean-src for nodeenv                |
|2018-03-03|[pre-commit#718]            |Refuse to install with core.hooksPath set  |
|2018-03-07|[pre-commit#720]            |Add a manual stage for cli-only interaction|
|2018-03-07|[pre-commit.github.io#157]  |Documentation updates for 1.7.0            |
|2018-03-08|[demo-repo#2]               |Normalize git urls in pre-commit config    |
|2018-03-08|[pre-commit#721]            |Normalize git urls in pre-commit config    |
|2018-03-09|[cron-mirror-creation#3]    |Ran pre-commit autoupdate.                 |
|2018-03-09|[pre-commit#722]            |Ran pre-commit autoupdate.                 |
|2018-03-09|[pre-commit-hooks#272]      |Ran pre-commit autoupdate.                 |
|2018-03-09|[pre-commit-mirror-maker#26]|Ran pre-commit autoupdate.                 |
|2018-03-12|[pre-commit#724]            |Restore git 1.8 support                    |
|2018-03-12|[pre-commit#725]            |Fix go 1.10: no pkg dir                    |
|2018-03-12|[pre-commit#726]            |Fix typo                                   |
|2018-03-18|[pre-commit#729]            |Fix regression: try-repo from relative path|
|2018-03-19|[pre-commit-hooks#274]      |Add an `--unsafe` option to `check-yaml`   |
|2018-03-26|[pre-commit-hooks#277]      |Always load the README as UTF-8            |
|2018-03-26|[pre-commit-hooks#280]      |pull with --no-rebase                      |
|2018-03-26|[pre-commit-hooks#281]      |Remove write_file (now unnecessary)        |
|2018-03-29|[pre-commit.github.io#159]  |Add jorisroovers/gitlint to list of hooks  |


### april

|date      |link                        |title                        |
|----------|----------------------------|-----------------------------|
|2018-04-04|[pre-commit.github.io#160]  |Add ambv/black               |
|2018-04-26|[pre-commit.github.io#161]  |Document log_file hook option|
|2018-04-30|[pre-commit#740]            |Replace legacy wheel metadata|
|2018-04-30|[pre-commit-hooks#282]      |Replace legacy wheel metadata|
|2018-04-30|[pre-commit-mirror-maker#28]|Replace legacy wheel metadata|


### may

|date      |link                        |title                                                           |
|----------|----------------------------|----------------------------------------------------------------|
|2018-05-02|[pre-commit#741]            |Remove unused __popen DI                                        |
|2018-05-12|[pre-commit#750]            |Apply relative files to try-repo also                           |
|2018-05-13|[pre-commit.github.io#162]  |Add asottile/seed-isort-config                                  |
|2018-05-14|[mirrors-isort#2]           |Mention seed-isort-config                                       |
|2018-05-14|[pre-commit-hooks#283]      |debug-statements: detect python3.7+ breakpoint()                |
|2018-05-18|[pre-commit-hooks#286]      |Explicitly check for `ast.Name`                                 |
|2018-05-20|[pre-commit-mirror-maker#29]|Drop python2 support                                            |
|2018-05-22|[pre-commit#752]            |Fix test since pip 10 changed output                            |
|2018-05-22|[pre-commit-mirror-maker#30]|Add support for --types                                         |
|2018-05-22|[pre-commit.github.io#164]  |Document the python_venv language                               |
|2018-05-24|[pre-commit#753]            |Remove (unused) Makefile                                        |
|2018-05-24|[pre-commit-hooks#288]      |Remove (unused) Makefile                                        |
|2018-05-25|[pre-commit#754]            |pytest: drop the dot!                                           |
|2018-05-25|[pre-commit-mirror-maker#35]|pytest: drop the dot!                                           |
|2018-05-26|[pre-commit-mirror-maker#36]|Don't use the deprecated xmlrpc pypi api                        |
|2018-05-28|[pre-commit#756]            |Invoke -mvenv with the original python if in a -mvirtualenv venv|
|2018-05-28|[pre-commit-docker-flake8#2]|Suggest https:// git urls                                       |
|2018-05-28|[pre-commit-hooks#289]      |Suggest https:// git urls                                       |


### june

|date      |link                        |title                                     |
|----------|----------------------------|------------------------------------------|
|2018-06-01|[pre-commit#759]            |E309 is no longer rewritten by autopep8   |
|2018-06-01|[pre-commit-hooks#290]      |E309 is no longer rewritten by autopep8   |
|2018-06-01|[pre-commit-mirror-maker#37]|E309 is no longer an error in autopep8    |
|2018-06-02|[pre-commit#760]            |Include README as long_description        |
|2018-06-03|[pre-commit-mirror-maker#38]|Add types                                 |
|2018-06-03|[pre-commit.github.io#167]  |Add asottile/blacken-docs                 |
|2018-06-04|[pre-commit#762]            |Simplify setup.py in arbitrary_bytes_repo |
|2018-06-04|[pre-commit-hooks#293]      |Improve vcs regex (don't match whitespace)|
|2018-06-06|[pre-commit#764]            |Move testing scripts into testing         |
|2018-06-09|[pre-commit-hooks#294]      |Allow multiple branches to be protected   |
|2018-06-10|[pre-commit.github.io#169]  |Fix typos                                 |
|2018-06-11|[pre-commit#767]            |Consistent ordering of filenames          |
|2018-06-14|[cron-mirror-creation#4]    |Default --scripts-are-modules for mypy    |
|2018-06-17|[pre-commit.github.io#170]  |Add types                                 |
|2018-06-18|[pre-commit#769]            |Fix invalid escape sequences              |
|2018-06-18|[pre-commit-hooks#296]      |Fix invalid escape sequences              |
|2018-06-18|[pre-commit-hooks#297]      |Fix resource warnings                     |
|2018-06-21|[mirrors-autopep8#1]        |Replace sha: with rev: in documentation   |
|2018-06-21|[mirrors-coffeelint#4]      |Replace sha: with rev: in documentation   |
|2018-06-21|[mirrors-csslint#1]         |Replace sha: with rev: in documentation   |
|2018-06-21|[mirrors-eslint#12]         |Replace sha: with rev: in documentation   |
|2018-06-21|[mirrors-fixmyjs#1]         |Replace sha: with rev: in documentation   |
|2018-06-21|[mirrors-jshint#5]          |Replace sha: with rev: in documentation   |
|2018-06-21|[mirrors-puppet-lint#1]     |Replace sha: with rev: in documentation   |
|2018-06-21|[mirrors-pylint#8]          |Replace sha: with rev: in documentation   |
|2018-06-21|[mirrors-ruby-lint#1]       |Replace sha: with rev: in documentation   |
|2018-06-21|[mirrors-scss-lint#3]       |Replace sha: with rev: in documentation   |
|2018-06-21|[mirrors-yapf#7]            |Replace sha: with rev: in documentation   |
|2018-06-27|[pre-commit-docker-flake8#3]|sha -> rev (pre-commit 1.7.0+)            |
|2018-06-30|[pre-commit#773]            |Separate store from runner                |


### july

|date      |link                        |title                                                                        |
|----------|----------------------------|-----------------------------------------------------------------------------|
|2018-07-02|[pre-commit#774]            |Remove more properties from Runner                                           |
|2018-07-02|[pre-commit#778]            |Fix force-push without fetch                                                 |
|2018-07-03|[pre-commit#779]            |Appease yaml.load linters                                                    |
|2018-07-04|[pre-commit#785]            |Improve not found error with script paths (`./exe`)                          |
|2018-07-04|[pre-commit#786]            |Oops, this wrote a hash.txt file to the working dir                          |
|2018-07-04|[pre-commit.github.io#173]  |Move the "Developing hooks interactively" section higher                     |
|2018-07-05|[pre-commit#787]            |hook paths are only computed in install_uninstall                            |
|2018-07-05|[pre-commit#788]            |Cache rust installation on windows too                                       |
|2018-07-08|[pre-commit#790]            |Don't test python3.5 now that we test python3.7                              |
|2018-07-08|[pre-commit#791]            |tox 3.1 passes PROCESSOR_ARCHITECTURE by default                             |
|2018-07-08|[pre-commit-hooks#305]      |Don't test python3.5 now that we test python3.7                              |
|2018-07-10|[pre-commit#792]            |Use python3.7 in appveyor                                                    |
|2018-07-10|[pre-commit-hooks#306]      |Use python3.7 in appveyor                                                    |
|2018-07-14|[cron-mirror-creation#5]    |Upgrade mypy                                                                 |
|2018-07-14|[pre-commit-mirror-maker#40]|Upgrade mypy                                                                 |
|2018-07-18|[pre-commit#796]            |Fix buffering in --show-diff-on-failure                                      |
|2018-07-18|[pre-commit#797]            |Default to python3 when using python_venv under python 2                     |
|2018-07-18|[pre-commit#799]            |Temporarily xfail node on windows                                            |
|2018-07-18|[pre-commit#800]            |Revert "Merge pull request #788 from pre-commit/cache_cargo_windows"         |
|2018-07-19|[pre-commit#801]            |Revert "Merge pull request #799 from pre-commit/temporarily_skip_npm_windows"|
|2018-07-25|[pre-commit#805]            |Work around sys.executable issue using brew python on macos                  |
|2018-07-29|[pre-commit.github.io#176]  |Add pre-commit/pygrep-hooks repo                                             |


### august

|date      |link                        |title                                         |
|----------|----------------------------|----------------------------------------------|
|2018-08-06|[pre-commit#809]            |Support `pre-commit install` inside a worktree|
|2018-08-11|[cron-mirror-creation#6]    |Stricter mypy                                 |
|2018-08-11|[pre-commit#812]            |Add language: fail                            |
|2018-08-11|[pre-commit-mirror-maker#41]|Stricter mypy                                 |
|2018-08-16|[pre-commit#815]            |Update config                                 |


### september

|date      |link                      |title                                                |
|----------|--------------------------|-----------------------------------------------------|
|2018-09-03|[pre-commit#821]          | Exempt `language: fail` hooks from check-hooks-apply|
|2018-09-03|[pre-commit.github.io#181]|Document `language: fail`                            |
|2018-09-20|[pre-commit.github.io#183]|sassc -> pysassc                                     |
|2018-09-22|[pre-commit#832]          |Fix rev-parse for older git versions                 |


### october

|date      |link                        |title                                                      |
|----------|----------------------------|-----------------------------------------------------------|
|2018-10-04|[pygrep-hooks#1]            |Improve python-use-type-annotations                        |
|2018-10-07|[pre-commit.github.io#187]  |Remove broken links                                        |
|2018-10-11|[pre-commit#844]            |fix pushing to new branch not identifying all commits      |
|2018-10-13|[cron-mirror-creation#7]    |Migrate from autopep8-wrapper to mirrors-autopep8          |
|2018-10-13|[pre-commit#845]            |Migrate from autopep8-wrapper to mirrors-autopep8          |
|2018-10-13|[pre-commit-hooks#321]      |Remove autopep8-wrapper in favor of autopep8               |
|2018-10-13|[pre-commit-hooks#323]      |Remove legacy hooks.yaml and pre-types config              |
|2018-10-13|[pre-commit-hooks#324]      |Default --no-markdown-linebreak-ext for trailing-whitespace|
|2018-10-13|[pre-commit-hooks#325]      |Use subprocess directly                                    |
|2018-10-13|[pre-commit-installed#1]    |Migrate from autopep8-wrapper to mirrors-autopep8          |
|2018-10-13|[pre-commit-mirror-maker#42]|Migrate from autopep8-wrapper to mirrors-autopep8          |
|2018-10-13|[pygrep-hooks#2]            |Migrate from autopep8-wrapper to mirrors-autopep8          |
|2018-10-14|[pre-commit#846]            |Improve performance by factoring out pkg_resources         |
|2018-10-14|[pre-commit#847]            |Improve coverage of check_hooks_apply                      |
|2018-10-23|[pre-commit#852]            |Install multi-hook repositories only once                  |
|2018-10-29|[pre-commit.github.io#188]  |Add bandit to list of hook repos                           |


### november

|date      |link                      |title                    |
|----------|--------------------------|-------------------------|
|2018-11-09|[pre-commit.github.io#189]|Add miki725/importanize  |
|2018-11-16|[pre-commit#870]          |Upgrade the sample config|
|2018-11-22|[pre-commit.github.io#191]|Add PyCQA/flake8         |


### december

|date      |link                        |title                                                        |
|----------|----------------------------|-------------------------------------------------------------|
|2018-12-19|[pre-commit#889]            |Switch from deprecated docs-off args to --no-document        |
|2018-12-20|[pre-commit#888]            |xfail windows node until #887 is resolved                    |
|2018-12-25|[pre-commit-mirror-maker#43]|gem name may not start with an underscore                    |
|2018-12-26|[pre-commit#893]            |Pick a better python shebang for hook executable             |
|2018-12-26|[pre-commit.github.io#195]  |Add jinjalint                                                |
|2018-12-27|[pre-commit#895]            |Remove stateful Runner                                       |
|2018-12-28|[pre-commit#896]            |misc cleanup                                                 |
|2018-12-28|[pre-commit-hooks#351]      |switch from pyyaml to ruamel.yaml                            |
|2018-12-29|[pre-commit#898]            |Add identity meta hook                                       |
|2018-12-30|[pre-commit.github.io#197]  |Use pygments-pre-commit to highlight docs                    |
|2018-12-31|[pre-commit#899]            |Refactor pre_commit.repository and factor out cached-property|
|2018-12-31|[pre-commit#900]            |just use normal dicts in tests                               |
|2018-12-31|[pre-commit#901]            |Use Hook api in languages                                    |
|2018-12-31|[pre-commit#902]            |Add more 'no cover windows' comments                         |



[pre-commit#673]: https://github.com/pre-commit/pre-commit/pull/673
[pre-commit#674]: https://github.com/pre-commit/pre-commit/pull/674
[pre-commit#676]: https://github.com/pre-commit/pre-commit/pull/676
[pre-commit#680]: https://github.com/pre-commit/pre-commit/pull/680
[pre-commit#684]: https://github.com/pre-commit/pre-commit/pull/684
[pre-commit#685]: https://github.com/pre-commit/pre-commit/pull/685
[pre-commit#686]: https://github.com/pre-commit/pre-commit/pull/686
[pre-commit#687]: https://github.com/pre-commit/pre-commit/pull/687
[pre-commit#688]: https://github.com/pre-commit/pre-commit/pull/688
[pre-commit.github.io#152]: https://github.com/pre-commit/pre-commit.github.io/pull/152
[pre-commit-mirror-maker#25]: https://github.com/pre-commit/pre-commit-mirror-maker/pull/25
[pre-commit#690]: https://github.com/pre-commit/pre-commit/pull/690
[pre-commit-hooks#259]: https://github.com/pre-commit/pre-commit-hooks/pull/259
[pre-commit#694]: https://github.com/pre-commit/pre-commit/pull/694
[pre-commit#698]: https://github.com/pre-commit/pre-commit/pull/698
[pre-commit-hooks#261]: https://github.com/pre-commit/pre-commit-hooks/pull/261
[pre-commit.github.io#153]: https://github.com/pre-commit/pre-commit.github.io/pull/153
[pre-commit#699]: https://github.com/pre-commit/pre-commit/pull/699
[pre-commit.github.io#156]: https://github.com/pre-commit/pre-commit.github.io/pull/156
[pre-commit#700]: https://github.com/pre-commit/pre-commit/pull/700
[pre-commit-hooks#266]: https://github.com/pre-commit/pre-commit-hooks/pull/266
[pre-commit#710]: https://github.com/pre-commit/pre-commit/pull/710
[pre-commit#712]: https://github.com/pre-commit/pre-commit/pull/712
[pre-commit-hooks#269]: https://github.com/pre-commit/pre-commit-hooks/pull/269
[pre-commit#711]: https://github.com/pre-commit/pre-commit/pull/711
[pre-commit#713]: https://github.com/pre-commit/pre-commit/pull/713
[pre-commit#714]: https://github.com/pre-commit/pre-commit/pull/714
[pre-commit#715]: https://github.com/pre-commit/pre-commit/pull/715
[pre-commit-hooks#271]: https://github.com/pre-commit/pre-commit-hooks/pull/271
[pre-commit#717]: https://github.com/pre-commit/pre-commit/pull/717
[pre-commit#718]: https://github.com/pre-commit/pre-commit/pull/718
[pre-commit#720]: https://github.com/pre-commit/pre-commit/pull/720
[pre-commit.github.io#157]: https://github.com/pre-commit/pre-commit.github.io/pull/157
[demo-repo#2]: https://github.com/pre-commit/demo-repo/pull/2
[pre-commit#721]: https://github.com/pre-commit/pre-commit/pull/721
[cron-mirror-creation#3]: https://github.com/pre-commit/cron-mirror-creation/pull/3
[pre-commit#722]: https://github.com/pre-commit/pre-commit/pull/722
[pre-commit-hooks#272]: https://github.com/pre-commit/pre-commit-hooks/pull/272
[pre-commit-mirror-maker#26]: https://github.com/pre-commit/pre-commit-mirror-maker/pull/26
[pre-commit#724]: https://github.com/pre-commit/pre-commit/pull/724
[pre-commit#725]: https://github.com/pre-commit/pre-commit/pull/725
[pre-commit#726]: https://github.com/pre-commit/pre-commit/pull/726
[pre-commit#729]: https://github.com/pre-commit/pre-commit/pull/729
[pre-commit-hooks#274]: https://github.com/pre-commit/pre-commit-hooks/pull/274
[pre-commit-hooks#277]: https://github.com/pre-commit/pre-commit-hooks/pull/277
[pre-commit-hooks#280]: https://github.com/pre-commit/pre-commit-hooks/pull/280
[pre-commit-hooks#281]: https://github.com/pre-commit/pre-commit-hooks/pull/281
[pre-commit.github.io#159]: https://github.com/pre-commit/pre-commit.github.io/pull/159
[pre-commit.github.io#160]: https://github.com/pre-commit/pre-commit.github.io/pull/160
[pre-commit.github.io#161]: https://github.com/pre-commit/pre-commit.github.io/pull/161
[pre-commit#740]: https://github.com/pre-commit/pre-commit/pull/740
[pre-commit-hooks#282]: https://github.com/pre-commit/pre-commit-hooks/pull/282
[pre-commit-mirror-maker#28]: https://github.com/pre-commit/pre-commit-mirror-maker/pull/28
[pre-commit#741]: https://github.com/pre-commit/pre-commit/pull/741
[pre-commit#750]: https://github.com/pre-commit/pre-commit/pull/750
[pre-commit.github.io#162]: https://github.com/pre-commit/pre-commit.github.io/pull/162
[mirrors-isort#2]: https://github.com/pre-commit/mirrors-isort/pull/2
[pre-commit-hooks#283]: https://github.com/pre-commit/pre-commit-hooks/pull/283
[pre-commit-hooks#286]: https://github.com/pre-commit/pre-commit-hooks/pull/286
[pre-commit-mirror-maker#29]: https://github.com/pre-commit/pre-commit-mirror-maker/pull/29
[pre-commit#752]: https://github.com/pre-commit/pre-commit/pull/752
[pre-commit-mirror-maker#30]: https://github.com/pre-commit/pre-commit-mirror-maker/pull/30
[pre-commit.github.io#164]: https://github.com/pre-commit/pre-commit.github.io/pull/164
[pre-commit#753]: https://github.com/pre-commit/pre-commit/pull/753
[pre-commit-hooks#288]: https://github.com/pre-commit/pre-commit-hooks/pull/288
[pre-commit#754]: https://github.com/pre-commit/pre-commit/pull/754
[pre-commit-mirror-maker#35]: https://github.com/pre-commit/pre-commit-mirror-maker/pull/35
[pre-commit-mirror-maker#36]: https://github.com/pre-commit/pre-commit-mirror-maker/pull/36
[pre-commit#756]: https://github.com/pre-commit/pre-commit/pull/756
[pre-commit-docker-flake8#2]: https://github.com/pre-commit/pre-commit-docker-flake8/pull/2
[pre-commit-hooks#289]: https://github.com/pre-commit/pre-commit-hooks/pull/289
[pre-commit#759]: https://github.com/pre-commit/pre-commit/pull/759
[pre-commit-hooks#290]: https://github.com/pre-commit/pre-commit-hooks/pull/290
[pre-commit-mirror-maker#37]: https://github.com/pre-commit/pre-commit-mirror-maker/pull/37
[pre-commit#760]: https://github.com/pre-commit/pre-commit/pull/760
[pre-commit-mirror-maker#38]: https://github.com/pre-commit/pre-commit-mirror-maker/pull/38
[pre-commit.github.io#167]: https://github.com/pre-commit/pre-commit.github.io/pull/167
[pre-commit#762]: https://github.com/pre-commit/pre-commit/pull/762
[pre-commit-hooks#293]: https://github.com/pre-commit/pre-commit-hooks/pull/293
[pre-commit#764]: https://github.com/pre-commit/pre-commit/pull/764
[pre-commit-hooks#294]: https://github.com/pre-commit/pre-commit-hooks/pull/294
[pre-commit.github.io#169]: https://github.com/pre-commit/pre-commit.github.io/pull/169
[pre-commit#767]: https://github.com/pre-commit/pre-commit/pull/767
[cron-mirror-creation#4]: https://github.com/pre-commit/cron-mirror-creation/pull/4
[pre-commit.github.io#170]: https://github.com/pre-commit/pre-commit.github.io/pull/170
[pre-commit#769]: https://github.com/pre-commit/pre-commit/pull/769
[pre-commit-hooks#296]: https://github.com/pre-commit/pre-commit-hooks/pull/296
[pre-commit-hooks#297]: https://github.com/pre-commit/pre-commit-hooks/pull/297
[mirrors-autopep8#1]: https://github.com/pre-commit/mirrors-autopep8/pull/1
[mirrors-coffeelint#4]: https://github.com/pre-commit/mirrors-coffeelint/pull/4
[mirrors-csslint#1]: https://github.com/pre-commit/mirrors-csslint/pull/1
[mirrors-eslint#12]: https://github.com/pre-commit/mirrors-eslint/pull/12
[mirrors-fixmyjs#1]: https://github.com/pre-commit/mirrors-fixmyjs/pull/1
[mirrors-jshint#5]: https://github.com/pre-commit/mirrors-jshint/pull/5
[mirrors-puppet-lint#1]: https://github.com/pre-commit/mirrors-puppet-lint/pull/1
[mirrors-pylint#8]: https://github.com/pre-commit/mirrors-pylint/pull/8
[mirrors-ruby-lint#1]: https://github.com/pre-commit/mirrors-ruby-lint/pull/1
[mirrors-scss-lint#3]: https://github.com/pre-commit/mirrors-scss-lint/pull/3
[mirrors-yapf#7]: https://github.com/pre-commit/mirrors-yapf/pull/7
[pre-commit-docker-flake8#3]: https://github.com/pre-commit/pre-commit-docker-flake8/pull/3
[pre-commit#773]: https://github.com/pre-commit/pre-commit/pull/773
[pre-commit#774]: https://github.com/pre-commit/pre-commit/pull/774
[pre-commit#778]: https://github.com/pre-commit/pre-commit/pull/778
[pre-commit#779]: https://github.com/pre-commit/pre-commit/pull/779
[pre-commit#785]: https://github.com/pre-commit/pre-commit/pull/785
[pre-commit#786]: https://github.com/pre-commit/pre-commit/pull/786
[pre-commit.github.io#173]: https://github.com/pre-commit/pre-commit.github.io/pull/173
[pre-commit#787]: https://github.com/pre-commit/pre-commit/pull/787
[pre-commit#788]: https://github.com/pre-commit/pre-commit/pull/788
[pre-commit#790]: https://github.com/pre-commit/pre-commit/pull/790
[pre-commit#791]: https://github.com/pre-commit/pre-commit/pull/791
[pre-commit-hooks#305]: https://github.com/pre-commit/pre-commit-hooks/pull/305
[pre-commit#792]: https://github.com/pre-commit/pre-commit/pull/792
[pre-commit-hooks#306]: https://github.com/pre-commit/pre-commit-hooks/pull/306
[cron-mirror-creation#5]: https://github.com/pre-commit/cron-mirror-creation/pull/5
[pre-commit-mirror-maker#40]: https://github.com/pre-commit/pre-commit-mirror-maker/pull/40
[pre-commit#796]: https://github.com/pre-commit/pre-commit/pull/796
[pre-commit#797]: https://github.com/pre-commit/pre-commit/pull/797
[pre-commit#799]: https://github.com/pre-commit/pre-commit/pull/799
[pre-commit#800]: https://github.com/pre-commit/pre-commit/pull/800
[pre-commit#801]: https://github.com/pre-commit/pre-commit/pull/801
[pre-commit#805]: https://github.com/pre-commit/pre-commit/pull/805
[pre-commit.github.io#176]: https://github.com/pre-commit/pre-commit.github.io/pull/176
[pre-commit#809]: https://github.com/pre-commit/pre-commit/pull/809
[cron-mirror-creation#6]: https://github.com/pre-commit/cron-mirror-creation/pull/6
[pre-commit#812]: https://github.com/pre-commit/pre-commit/pull/812
[pre-commit-mirror-maker#41]: https://github.com/pre-commit/pre-commit-mirror-maker/pull/41
[pre-commit#815]: https://github.com/pre-commit/pre-commit/pull/815
[pre-commit#821]: https://github.com/pre-commit/pre-commit/pull/821
[pre-commit.github.io#181]: https://github.com/pre-commit/pre-commit.github.io/pull/181
[pre-commit.github.io#183]: https://github.com/pre-commit/pre-commit.github.io/pull/183
[pre-commit#832]: https://github.com/pre-commit/pre-commit/pull/832
[pygrep-hooks#1]: https://github.com/pre-commit/pygrep-hooks/pull/1
[pre-commit.github.io#187]: https://github.com/pre-commit/pre-commit.github.io/pull/187
[pre-commit#844]: https://github.com/pre-commit/pre-commit/pull/844
[cron-mirror-creation#7]: https://github.com/pre-commit/cron-mirror-creation/pull/7
[pre-commit#845]: https://github.com/pre-commit/pre-commit/pull/845
[pre-commit-hooks#321]: https://github.com/pre-commit/pre-commit-hooks/pull/321
[pre-commit-hooks#323]: https://github.com/pre-commit/pre-commit-hooks/pull/323
[pre-commit-hooks#324]: https://github.com/pre-commit/pre-commit-hooks/pull/324
[pre-commit-hooks#325]: https://github.com/pre-commit/pre-commit-hooks/pull/325
[pre-commit-installed#1]: https://github.com/pre-commit/pre-commit-installed/pull/1
[pre-commit-mirror-maker#42]: https://github.com/pre-commit/pre-commit-mirror-maker/pull/42
[pygrep-hooks#2]: https://github.com/pre-commit/pygrep-hooks/pull/2
[pre-commit#846]: https://github.com/pre-commit/pre-commit/pull/846
[pre-commit#847]: https://github.com/pre-commit/pre-commit/pull/847
[pre-commit#852]: https://github.com/pre-commit/pre-commit/pull/852
[pre-commit.github.io#188]: https://github.com/pre-commit/pre-commit.github.io/pull/188
[pre-commit.github.io#189]: https://github.com/pre-commit/pre-commit.github.io/pull/189
[pre-commit#870]: https://github.com/pre-commit/pre-commit/pull/870
[pre-commit.github.io#191]: https://github.com/pre-commit/pre-commit.github.io/pull/191
[pre-commit#889]: https://github.com/pre-commit/pre-commit/pull/889
[pre-commit#888]: https://github.com/pre-commit/pre-commit/pull/888
[pre-commit-mirror-maker#43]: https://github.com/pre-commit/pre-commit-mirror-maker/pull/43
[pre-commit#893]: https://github.com/pre-commit/pre-commit/pull/893
[pre-commit.github.io#195]: https://github.com/pre-commit/pre-commit.github.io/pull/195
[pre-commit#895]: https://github.com/pre-commit/pre-commit/pull/895
[pre-commit#896]: https://github.com/pre-commit/pre-commit/pull/896
[pre-commit-hooks#351]: https://github.com/pre-commit/pre-commit-hooks/pull/351
[pre-commit#898]: https://github.com/pre-commit/pre-commit/pull/898
[pre-commit.github.io#197]: https://github.com/pre-commit/pre-commit.github.io/pull/197
[pre-commit#899]: https://github.com/pre-commit/pre-commit/pull/899
[pre-commit#900]: https://github.com/pre-commit/pre-commit/pull/900
[pre-commit#901]: https://github.com/pre-commit/pre-commit/pull/901
[pre-commit#902]: https://github.com/pre-commit/pre-commit/pull/902
