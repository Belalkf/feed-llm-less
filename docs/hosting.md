# GitHub protections

This page describes the intended settings for [Belalkf/feed-llm-less](https://github.com/Belalkf/feed-llm-less). Check the live settings and workflow results before relying on them. The old project has separate settings.

## Main branch

Use an active `main-safety` ruleset for the default branch. Block deletion and force pushes. Require pull requests, resolved review threads, and the four Linux/macOS × Python 3.9/3.13 checks plus dependency review. Require current-base checks and CodeQL results without moderate-or-higher security alerts or code errors. Do not add a broad bypass. Zero required human approvals keeps this usable for a solo owner; it is not independent review.

Change code on a feature branch and merge only after checks and review. Keep the ruleset in step with job names. `python3 scripts/check_hosting.py` reads public branch rules with a 20-second timeout. It changes nothing. It checks branch policy, not every security setting or bypass, so also read the saved ruleset.

## Security checks

Use dependency alerts, malware alerts where available, and Dependabot security-update requests. Weekly version requests cover Actions and Python build tools. Review updates before merging; keep auto-merge off. Newer tools can drop older Python support, so check the declared minimum on Python 3.9 too.

Dependency review checks new known moderate-or-higher risks in pull requests. It uses read-only access, a five-minute job limit, and up to 120 seconds for dependency data retries. Missing data is a visible failure.

Use CodeQL for Python, JavaScript/TypeScript, and Actions, including local input checks. Inspect actual alerts; a green analysis job can still have findings. Keep supported secret scanning, push protection, and private vulnerability reporting enabled. A scanner cannot prove that there are no secrets or bugs.

## Workflow access

Keep default tokens read-only and stop workflows from approving pull requests. Require approval for external fork workflows. Give scanner jobs only the access they need. Use pinned official actions, bounded jobs, and cancellation for replaced runs. No personal token, third-party review bot, paid AI scan, or self-hosted runner is needed.

Leave generic secret patterns and provider validity calls off unless there is a clear need. Validity checks may contact the provider. Account-wide settings and notifications are outside this project's scope. Check costs before enabling optional features.

## Trust boundaries

The report tests execute this checkout's trusted JavaScript with a fixed command and timeout. Scanned projects never supply that code. The test VM is not a sandbox for hostile scripts. The release checker installs files from the folder chosen by the operator; use it only with trusted packages. Review these limits again if a service starts accepting outside input.

Read back live settings after saving, and inspect the default branch's job results and alerts. Configuration alone is not a passing check. See [support limits](readiness.md).

Sources: [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets), [dependency review](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review), and [CodeQL](https://docs.github.com/en/code-security/how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configure-code-scanning).
