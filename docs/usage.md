# Installation and everyday use

## Install an everyday command

From a copy of this repository, create a new Python environment. An environment keeps this tool separate from your other Python tools.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install 'setuptools>=58' wheel
python -m pip install --no-build-isolation --no-deps .
feed-llm-less --version
```

The build-tool step downloads setuptools and wheel. Skip it if they are already installed in your environment. Scans need no extra Python packages or network access. For a version listed on [PyPI](https://pypi.org/project/feed-llm-less/), you can instead run `python -m pip install feed-llm-less` in a new environment.

## Choose a project

```sh
feed-llm-less /path/to/project
feed-llm-less /path/to/project --terminal
feed-llm-less /path/to/project --plan --task "Make export easier to test"
```

Pass the Git root folder, not a subfolder. Without a path, the command uses your current folder. Bare repositories have no working files and are unsupported. Quote paths that contain spaces. The source command is `python3 -m feed_llm_less`, run from the tool checkout.

The browser report opens by default. Use `--no-open` to save without opening it, `--terminal` for a table, `--json` for structured data, or `--plan` for a ready-to-copy request. Use `--demo` for a report with made-up files. The macOS `.command` launcher asks for a project folder; it does not use a hidden project list. It adds no Finder Quick Action.

## Choose files for your agent

Open the report, add your goal, and copy the starter request. Pick specific files to replace that starting list. Filters change the table, not the request. Hidden selections stay selected. Open a file's hints when you need more detail.

Paste the request into an agent that can read the local project. A remote chat does not gain file access from the request alone. Ask the agent to explain what should stay together or change before editing. Keep your project's permission rules. The tool never runs the request itself.

Reports contain paths and file hashes, which help check whether a file changed. They contain no source text. Treat real reports as private; read the request before sharing. Rerun the scan to refresh it. Reloading the page keeps the same results. Delete temporary reports when done; there is no automatic cleanup or background service.

## More than one project

```sh
feed-llm-less /path/to/api /path/to/web --no-open
feed-llm-less --config examples/repositories.json --repo example-app --terminal
feed-llm-less /path/to/project --include-untracked --seconds 90 --max-mib 24
feed-llm-less /path/to/project --output new-report.html --no-open
```

Copy `examples/repositories.json` to an ignored `repositories.local.json` and add your own paths. Relative paths start beside the configuration file; home-folder expansion is supported. Use `--repo NAME` to select entries. Unselected missing folders do not block a scan. Duplicate JSON keys, repeated roots, unknown names, and unknown top-level keys are refused. Choose paths or configuration, not both. Projects with the same folder name need distinct names in a configuration.

`--output` creates a new private HTML file and refuses existing files or links. Shell output redirection follows your shell's own overwrite and permission rules.

## If something goes wrong

| What you see | Next step |
| --- | --- |
| Not a Git root | Choose the folder containing `.git`, or a worktree root |
| Git is missing | Install Git yourself; the tool never downloads it |
| Browser did not open | Open the printed HTML path, or use `--terminal` |
| Copy is blocked | Use the selected-text fallback and your copy shortcut |
| No matching files | Read the scan coverage, then choose “Show all sizes” |
| Incomplete scan | Read the gaps; raise a limit only when it makes sense |
| Missing or changed files | Finish edits and run the scan again |
| Output already exists | Choose a new filename; the old file stays safe |
| Native Windows | Use macOS or Linux; WSL has not been checked |

## Optional agent skill

Run `npx skills add Belalkf/feed-llm-less` with Node.js 22.20 or later. Choose your agent. The default is a project install; add `-g` for your account. Use `npx skills add /path/to/feed-llm-less --list` to check a local source copy. The installer may download its own package and the public skill. It does not install the Python tool.

See the [skills CLI](https://github.com/vercel-labs/skills) for current agent support and Node requirements. Its [FAQ](https://skills.sh/docs/faq) explains optional installation telemetry. This is separate from the offline scanner. Check your agent's privacy settings before sharing project details. A skill gives guidance, not a guarantee about an agent's behavior.
