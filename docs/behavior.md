# Measurement and safety contract

## Discovery

Each input must be a Git repo root. Git lists tracked paths with NUL separators, so names with spaces or newlines stay separate. The tool measures files as they are now, not the copies saved in Git. Add `--include-untracked` for new files that Git does not ignore. Tracked files are included even if an ignore rule now matches them. Paths with merge conflicts are counted once. Submodules appear as unmeasured entries; the tool does not scan inside them. Files missing from a sparse checkout leave a coverage gap.

Repos are scanned in input order. The default limits are 60 seconds and 100,000 attempted paths across all targets. Each Git call waits at most 10 seconds within the time left. Git's path list is held in memory before the path limit is applied. A slow file read can run past the time limit. Control-C stops the tool between operations that can be interrupted; the tool leaves no worker or background process running.

## Measurement

Only regular files are opened. File and directory symlinks are rejected. Text must be valid UTF-8. Files with invalid UTF-8 or NUL bytes are expected exclusions; other skipped files make coverage incomplete. Each file can be up to 16 MiB by default, adjustable to 1,024 MiB. Scan time can be set up to 3,600 seconds. The tool reads in chunks and checks file identity, size and timestamps before and after reading, then reopens the path to check again. This catches ordinary edits and replacement during a scan. It does not provide a fixed snapshot against hostile file changes.

LF, CRLF and CR each count as one line ending. A last line without an ending still counts; an empty file has zero lines. Blank lines and comments count too. File size and longest line use bytes, not characters, screen columns or AI tokens. Line-ending bytes do not count toward the longest line; a UTF-8 byte-order mark contributes bytes. The tool does not guess text encoding or open archives.

## Reports

Rows sort by line count, then file size, both largest first, followed by repo name and path. The terminal shows the first 50 measured text files. HTML starts with up to 250 matching rows and lets you show more. Selected files stay selected when a filter hides them. “Select visible” selects rows currently shown in the table, including those below the visible part of the page. Zero turns off one size condition; three zeroes show every size. If clipboard copying fails, you can select and copy the text instead.

Filters do not change coverage: an empty table does not mean every file was checked. HTML and JSON include absolute repo paths and SHA-256 fingerprints, but no source content. A fingerprint identifies the measured bytes. JSON uses `schema_version: 1` and includes UTC `created`, budgets, `repositories` coverage records and measured `rows`. Releases in 0.1.x may add keys; readers should ignore unknown keys. A breaking format change needs a new schema version. HTML is a saved snapshot; run the scan again to refresh it.

## Exit codes

| Code | Meaning |
| --- | --- |
| 0 | Inventory complete, with expected binary/non-UTF-8 exclusions allowed |
| 1 | Missing scan coverage or an output failure |
| 2 | Invalid arguments/configuration or unsupported platform |
| 130 | Stopped with Control-C |

If the browser cannot open, the report is kept and the tool explains how to open it yourself. That does not make a completed scan fail. Missing Git produces an incomplete inventory. An existing folder that is not a repo produces a gap and exit 1. A missing input folder is rejected before scanning with exit 2.

## Review guidance

By default, rows include hints based on paths and file formats, without reading source again. `--inventory-only` leaves out those hints. The tool does not parse a programming language or decide where a file should split. When one repo folder has at least three text files of 40 lines or fewer, it adds up to eight nearby-file links. Files with connected formats or names that suggest generated output are left out. These links help navigation; they do not prove that files were split too far.

`--plan` prints a starter request for up to 12 files. It puts files that need content review before those that need format or producer checks, then sorts by line count and stable path order. HTML starts with the same scope, regardless of table filters, and says so. Selecting files replaces that starter scope and includes every selection, even hidden rows. Clearing selection brings the starter back. `--task` adds a goal of up to 2,000 characters; you can edit it locally in HTML. The tool does not match files to the task. Review the proposed scope and change it when needed.

The copied request includes scan gaps, measurement limits and a reminder to read current source, project rules, callers, shared state, interfaces and tests. A fingerprint does not prove that code is correct or still current. The report stays a saved snapshot. The tool does not run an agent, parse code or change its structure. Token savings have not been measured.

Shared instructions appear once per request. File entries contain quoted paths, measurements, fingerprints and format warnings. Expandable table details keep navigation hints out of the copied request. Fixed rules build the request; the receiving agent supplies code understanding after reading the source.
