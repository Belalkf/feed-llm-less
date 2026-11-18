# Support and checks

Feed LLM Less is an early version. It needs Python 3.9+ and Git.

| System | Support |
| --- | --- |
| macOS | Supported; local checks run here |
| Linux | Supported; the hosted workflow checks it |
| Native Windows | Unsupported: safe file reading needs POSIX features |
| WSL | Not checked |

The [Checks workflow](https://github.com/Belalkf/feed-llm-less/actions/workflows/ci.yml) shows results for each published change. See [Contributing](../CONTRIBUTING.md) to run the same checks.

Tests use made-up projects. They cover the command, file reading, report controls, and package installation. They do not prove screen-reader support or how every browser looks. Mobile layout, Linux browser appearance, and the interactive Finder launcher still need checks. A screenshot is only a view of one demo.

There is no measured token saving or independent test of an agent's decisions. The tool measures files and gives path hints. It does not parse or change the code, or start an agent. See [scan details](behavior.md).

Repository scanners can find some problems. Passing them does not prove that there are no bugs, secrets, or security risks.
