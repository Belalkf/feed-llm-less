# Maintainer release guide

## Review the public boundary

Keep this project separate from earlier projects. Review copied changes first. Never copy private history or configuration, or sync projects automatically. Use a public or noreply address for both Git author and committer.

Review source, history, images, and package files for private details. Use made-up examples. A pattern scan cannot prove privacy. Keep real project reports out of the release. The [architecture](architecture.md#public-boundary) owns the public source boundary.

## Prepare a release

1. Run the [contributor checks](../CONTRIBUTING.md), review the complete diff and check compatibility with supported Python versions. Review licences and network behaviour if dependencies change.
2. Build fresh wheel and source archives, verify report assets, and try the installed command outside the source folder using the packaging instructions in Contributing.
3. Keep the version and [changelog](../CHANGELOG.md) aligned. Describe user-visible changes, fixes, compatibility and remaining limits; leave commit-by-commit execution logs in the pull request and CI.
4. Use a feature branch and protected pull request. Wait for current-base checks, inspect actual scanner findings and preserve the [hosting policy](hosting.md). Recheck current GitHub options when changing that policy.
5. Create an annotated version tag and GitHub release only within the authorized publication scope and after its checks pass. Keep published tags stable; fixes belong in later commits/releases.

## Publish to PyPI

Publishing needs explicit authorization and a PyPI account. Before the first upload, check the package name, metadata, rendered description and source/wheel contents. Configure a [pending trusted publisher](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/) on PyPI with project `feed-llm-less`, owner `Belalkf`, repository `feed-llm-less`, workflow `publish.yml` and environment `pypi`. This permits that repository workflow to publish this package without a stored API token; a pending publisher does not reserve the name.

In the GitHub repository's `pypi` environment, select **Selected branches and tags** and add only a **Branch** rule named `main`. This limits publishing to the chosen source in GitHub's environment settings as well as in the workflow; leave other branches and tags outside the publishing environment.

After the protected pull request and current-main checks pass, run by hand **Publish to PyPI** from `main` in GitHub Actions. Its default run only builds and validates the distributions. Enable **Upload checked distributions to PyPI** only after the account configuration is correct. A separate `pypi` job gets short-lived upload access and sends the checked package files. It does not download or run the project source. The workflow never runs automatically on a push or pull request, and it refuses other branches.

After success, check the PyPI version and hashes, install `feed-llm-less` from PyPI in a fresh virtual environment, and run the demo and installed-command checks. Record the exact source commit and workflow result in the release or pull request. An upload does not prove security or that people use the tool.

## Verify skill distribution

Check `npx skills add Belalkf/feed-llm-less --list` and installation for the intended agents against the public source. According to the [skills.sh FAQ](https://skills.sh/docs/faq), leaderboard listing depends on installation telemetry; verify the actual result and current rules. A public source repo does not prove a package release, a listing, or token savings.
