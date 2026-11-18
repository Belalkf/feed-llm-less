# Maintainer entry point

## English and commit messages

Use B1–B2 English only, never C1 or C2, for new or edited English. This includes UI text, docs, agent rules, comments, docstrings, test descriptions, replies, PR text, commits and handoffs. Use short sentences and common words. Keep exact code names, API names, commands and quoted errors unchanged.

Before each commit, read the changed prose and the actual commit message. Simplify hard wording as part of the same edit. Older text and commits are not style examples. Pass this rule to any worker taking over.

Keep commit titles within 50 characters. Use one short sentence of at most 15 words for the body, with the main reason or effect. Do not repeat the title or add file lists, test lists or a work diary. Put detailed results in existing status or QA notes.

Read README.md, docs/architecture.md and docs/behavior.md before changing behaviour. This repo must work on its own: do not rely on sibling folders, private paths, global preferences or outside work notes.

## Product boundary

The scanner reads local files. Never run scanned code, start agents, upload source, install packages at runtime or change scanned repos. Preserve originals, reject unsafe inputs and show coverage gaps clearly. Use made-up examples with no real user or repo details.

## Change discipline

Start with checks that open no window: use `python3 -m feed_llm_less --demo --no-open` and the offline control tests. Use a new browser profile for any headless report check. A visible browser handoff needs permission. Keep real reports private and outside Git.

Keep file discovery, safe measurement, display and command handling separate. Add a regression test for every bug fix. After editing, review the whole change and ordinary user journey, including bad inputs, cancellation, incomplete scans, names with markup and existing-file safety. Run focused checks that fit the change. State clearly when a check did not run.

Split files only where separate jobs make sense. Size alone does not require splitting data, connected formats or source that belongs together. Prefer a few clear owners to many scattered helpers. Keep authored source and docs below 150 lines. Explain any specific exception in docs/architecture.md, with a reason and a condition for review. Do not compress code or prose to meet the count. Keep documentation paragraphs on one line.

## Delivery

Use the commands in CONTRIBUTING.md. Keep jobs owned, cancellable and time-limited. Preserve unrelated work and existing protections. Do not download dependencies or publish without permission. Check staged files and Git names and emails for private details before committing. Report what works, what is missing and what was actually tested separately. Do not start new agent sessions automatically.
