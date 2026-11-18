# Feed LLM Less

Give your coding agent a smaller place to start.

Big projects are easy to overfeed to an AI. Feed LLM Less lists your local files, shows which ones may need a closer look, and builds a review request you can copy into your agent. You choose the files. The agent still needs to read the code before making changes.

![A demo report with made-up project files](https://github.com/Belalkf/feed-llm-less/raw/main/docs/preview.png)

## Add it to your agent

```sh
npx skills add Belalkf/feed-llm-less
```

You need Node.js 22.20 or later. Choose your agent when asked. Add `-g` to use the skill across your projects. This installs the instructions; install the Python tool below to run scans.

## Try it

You need Python 3.9+, Git, and macOS or Linux. From a copy of this repository:

```sh
python3 -m feed_llm_less --demo
```

The demo uses made-up files. To review your own project, pass its Git root folder:

```sh
python3 -m feed_llm_less /path/to/project
```

Pick files in the report, add what you want to change, and copy the request into your coding agent. It can suggest keeping a file together, splitting it, combining small files, or simply reading less at once.

For a command you can run from any folder, see [installation and everyday use](https://github.com/Belalkf/feed-llm-less/blob/main/docs/usage.md).

## What it does

- Shows file sizes, line counts, filters, and missing scan results.
- Makes a short starting request, with your own file choices when needed.
- Runs offline and leaves your project files alone.
- Works with readable text in any language, without trying to understand every language.

A big file is a reason to look, not a reason to split. The name describes the goal; there is no measured token-saving claim. No model runs inside this tool.

Reports include local paths and file details, so review them before sharing. Files that cannot be read stay visible as gaps. Native Windows is unsupported; WSL has not been checked.

[Usage](https://github.com/Belalkf/feed-llm-less/blob/main/docs/usage.md) · [How scanning works](https://github.com/Belalkf/feed-llm-less/blob/main/docs/behavior.md) · [Support](https://github.com/Belalkf/feed-llm-less/blob/main/docs/readiness.md) · [Contributing](https://github.com/Belalkf/feed-llm-less/blob/main/CONTRIBUTING.md) · [Security](https://github.com/Belalkf/feed-llm-less/blob/main/SECURITY.md)

MIT licensed.
