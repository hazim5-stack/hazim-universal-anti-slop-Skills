# Agent Instructions

This repository is created and curated by Hazim Batwa, Software Engineering Expert.

- Keep all code, comments, documentation, configuration, and test messages in English.
- Preserve the focused-skill architecture; do not merge all rules into one prompt.
- Update `registry/skills.json` whenever skills or presets change.
- Run repository validation and tests before reporting completion.
- Report defects rather than alleged AI authorship.
- Do not import third-party text or code without checking its license and recording provenance.

## GitHub operations in ChatGPT Work

- Use the connected GitHub integration for repository writes, including file updates, commits, branches, and pull requests.
- Do not run an interactive `git push` from the shell. The shell checkout does not inherit the GitHub integration credentials and may wait indefinitely for authentication.
- When a read-only shell Git command is necessary, set `GIT_TERMINAL_PROMPT=0` so authentication failures return immediately instead of blocking the task.
- Keep GitHub writes small and sequential. Verify the resulting commit or file after each write before reporting completion.
- For binary assets, create Git blobs and one atomic tree commit through the GitHub integration; do not print binary or base64 content into the conversation.
