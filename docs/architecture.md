# Architecture

Data moves from the command to file discovery and measurement, then to report data and display. Scanned code is never imported. There is no server or remote API.

| Owner | Job |
| --- | --- |
| `feed_llm_less/cli.py` | Arguments, input checks, exit codes and cancellation |
| `feed_llm_less/config.py` | Chosen targets and user-owned settings |
| `feed_llm_less/scan.py` | Git file lists, counts, limits and row order |
| `feed_llm_less/measure.py` | Safe regular-file reads and text measurements |
| `feed_llm_less/analysis/` | Path hints for any language and nearby-file links |
| `feed_llm_less/briefing.py` | Shared agent instructions, priority and terminal request |
| `feed_llm_less/render.py` | Standalone HTML and safe data escaping |
| `feed_llm_less/output.py` | Private report files and terminal display |
| `feed_llm_less/report.*` | Browser layout, filters, selection and copying |
| `feed_llm_less/demo.py` | Made-up example data only |

## Organization decisions

File size is a reason to look, not a reason to split. Split when separate jobs make normal changes easier to follow. Keep connected formats, generated files, closely related tests and data together when splitting would break their use or meaning. Join small fragments when they make one job harder to find. The scanner cannot make those choices from size, and the copied request says so.

There are no language parsers. Path and format hints are starting points for review and work the same way across languages. Nearby-file links are navigation help, not a map of code dependencies. The tool is written in Python but can measure readable text in other languages.

The report's JavaScript stays together because filters, selection and page state form one small job. Revisit that choice if a separate interaction grows. HTML, CSS and JavaScript have separate source files and are bundled into one report. Keep CSS readable, with normal rule blocks rather than long compressed lines. No current authored file needs an exception to the 150-line limit. Example screenshots are image assets, not source files.

## Distribution

`pyproject.toml` selects the setuptools build tool. `setup.cfg` owns package details, bundled assets and the `feed-llm-less` command. This uses the available build tools without needing newer package-metadata support in the runtime Python version. No extra Python packages are needed at runtime. Both wheel and source archive must include all three report assets. The source archive also includes the optional skill; the Python wheel does not need to install agent instructions. Package details contain no personal author name or email.

The command-line tool is the main product. The optional skill in `skills/feed-llm-less/` helps compatible agents find its workflow. It adds no app logic or runtime dependency. Keeping both in one repo makes their behaviour easier to review together. You can still copy the report's request without installing a skill. GitHub skill installation and Python package installation are separate routes; see the README for the current commands.

## Public boundary

This edition contains selected source and tests with a fresh Git history. Old commits, private settings and shared-workspace instructions do not belong here. Review future patches before bringing them across; do not sync automatically with another checkout. See [releasing](releasing.md) for source and history checks before publication.
