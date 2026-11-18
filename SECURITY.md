# Security and privacy

The current 0.1.x line gets fixes when possible. This tool is not a security audit, a malware sandbox or a promise to stop within an exact time.

## Reporting a vulnerability

Use **Security → Advisories → Report a vulnerability** on [GitHub](https://github.com/Belalkf/feed-llm-less/security/advisories). If private reporting is unavailable, open an issue asking for a private route. Keep attack details, private paths and source content out of that public issue. No personal email or outside reporting service is included here.

## Trust boundary

The app never imports scanned code or starts an AI tool. It uses installed Git only to list paths. It removes inherited Git variables that could redirect the scan, disables global/system Git settings and disables filesystem-monitor hooks. Git still reads the repo's own data and settings. Keep Git updated and scan repos you trust; this tool does not make hostile repos safe.

File reads reject symlinks and non-regular files, and check for ordinary changes during measurement. This reduces accidental access through links and stale results. It does not guarantee a fixed snapshot against hostile file changes. Storage or Git can stall past the tool's time limits. Git's path list is held in memory before the attempted-file limit is applied. Avoid huge or hostile repos on machines with limited memory.

The HTML report escapes markup, displays labels as text and blocks outside connections through its content policy. A hostile filename can still mislead a person or an AI when copied elsewhere. Review copied requests and treat quoted paths as data. Real reports contain sensitive names and absolute paths. Sharing through the clipboard is your choice; the tool sends no report to a remote service.

## Files created

HTML output creates a new file with owner-only permissions where supported. The tool never replaces an existing path or automatically deletes a real report. A write failure may leave a partial file created by this run; remove it before retrying. JSON saved with shell redirection follows your shell's rules. Never publish real scan output in issues, screenshots or commits.

## Repository safeguards

[GitHub protections](docs/hosting.md) covers branch rules, dependency alerts and updates, CodeQL, secret scanning, workflow access and their limits. Preserve the useful protections when changing workflows, and check actual settings before claiming they are enabled.
