# Cross-agent installation — 2026-10-03

Skills CLI 1.7.0 on Windows installed all five skills from the local checkout
with `--copy -y` in an isolated temporary project. Targets: Claude Code, Codex,
Cursor, GitHub Copilot, Gemini CLI, OpenCode and Windsurf. Every source file,
including references, license and optional UI metadata, matched its installed
copy byte for byte. The CLI shares `.agents/skills/` among several destinations;
this was five packages in three destination trees, not seven model executions.
See [machine-readable results](cross-agent-install-2026-10-03.json).

The ZIP regression check confirms five archives, a single correctly named
folder per archive, safe relative paths, complete source bytes and reproducible
hashes. ZIPs are downloadable from the [Sepehra page](https://sepehra.ir/skills/#install).

No Claude account upload, Claude model run, other-agent model run or global
installation was performed. This records installation and packaging, not
cross-model output quality. Existing [behavioral evaluations](iran-context-2026-10-03/review.md)
remain separately scoped. No user-wide skills or settings were changed.
