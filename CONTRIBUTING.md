# Contributing

Help people review local code without changing the projects being scanned. Read [AGENTS.md](AGENTS.md), the [code map](docs/architecture.md), and the [scan rules](docs/behavior.md) first.

## Run checks

```sh
python3 -m unittest discover -s tests -v
node --test tests/test_*.cjs
python3 scripts/check_public.py
python3 -m feed_llm_less --demo --no-open
```

Python tests need no extra packages. Node 20+ is needed for report-control tests. Tests use temporary made-up projects. Never commit real reports or private configuration. These checks do not replace visual or screen-reader review.

For a bug, explain what a person sees. Add a test that fails before the fix, then check the whole change and related failure paths. Use plain English and keep each file's job clear. Keep document paragraphs on one line. Do not add downloads, network behavior, or dependencies without a clear need and permission.

## Check packaging

With setuptools and wheel installed, build into a new empty `dist` folder:

```sh
python3 -c "from setuptools.build_meta import build_wheel; build_wheel('dist')"
python3 -c "from setuptools.build_meta import build_sdist; build_sdist('dist')"
python3 scripts/check_wheel.py dist
```

This builds local files; it does not publish. The checker rebuilds the source archive without a package index and tests both wheels in a temporary environment. It needs pip, setuptools, and wheel. Run source and privacy checks first. For an installed skills CLI, use `npx --no-install skills add . --list` to avoid a new download.

## Send a change

Use a feature branch and pull request. Wait for current checks, resolve review threads, and review changes before merging. Keep the [branch and security policy](docs/hosting.md). Automated checks are not a person's review.

For an issue, include your OS, Python and Git versions, command, expected result, actual result, and exit code. Use made-up filenames and remove private details. Send security concerns through [SECURITY.md](SECURITY.md).

Contributions use the project's MIT license. Be respectful and focus on useful changes. There is no promised response time or long-term support.
