# Installation and compatibility

## Skills CLI

Requires Git and Node satisfying the current [CLI package](https://github.com/vercel-labs/skills). CLI discovery of the five packages has been checked; it is separate from executing every skill on every agent.

```bash
npx skills@latest add sajadjanat/iran-market-skills
npx skills@latest add sajadjanat/iran-market-skills --skill persian-rtl-ux --agent codex
npx skills@latest add sajadjanat/iran-market-skills --list
```

On PowerShell, use `npx.cmd` if execution policy blocks the npm PowerShell wrapper. Copy mode can be useful when symlinks are unavailable.

## Claude Code

Install all five through the CLI, or replace `'*'` with one skill name:

```bash
npx skills@latest add sajadjanat/iran-market-skills --skill '*' --agent claude-code
```

In Claude Code, invoke `/persian-rtl-ux` with a file or describe a relevant task.
For manual project installation, copy each complete `skills/<name>` directory
into `.claude/skills/<name>/`; for personal installation use
`~/.claude/skills/<name>/`. Keep `references/` and `LICENSE` with `SKILL.md`.
See [Claude Code's official skill documentation](https://code.claude.com/docs/en/skills).

## Claude web/desktop (claude.ai)

Download one skill ZIP from the [Sepehra page](https://sepehra.ir/skills/#install).
In Claude, enable code execution/file creation if required, then open
**Customize → Skills → + Create skill → Upload a skill**. Upload the ZIP and
turn the skill on. Availability depends on account and organization settings;
see [Claude's official instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).
Use a plain request such as “Use persian-brand-copy to rewrite this payment message.”
These are separate per-skill uploads, not the GitHub repository ZIP.

To create the same five archives locally (Python standard library only):

```bash
python scripts/package_skills.py
```

Each `dist/<name>.zip` contains one top-level skill folder, its unchanged
instructions, references and license. No API key, paid integration or model
connection is included. Desktop/web upload was not performed in a Claude account.

## Other agents and a manual fallback

The same `SKILL.md` packages can be installed through the CLI for its supported
agents. For example:

```bash
npx skills@latest add sajadjanat/iran-market-skills --skill '*' --agent cursor
npx skills@latest add sajadjanat/iran-market-skills --skill '*' --agent github-copilot
npx skills@latest add sajadjanat/iran-market-skills --skill '*' --agent gemini-cli
npx skills@latest add sajadjanat/iran-market-skills --skill '*' --agent opencode
npx skills@latest add sajadjanat/iran-market-skills --skill '*' --agent windsurf
```

The interactive command lets you choose other destinations; check the current
[CLI agent list](https://github.com/vercel-labs/skills#supported-agents).
For tools without native skill loading, attach `SKILL.md` and the references
needed for the task, then explicitly ask the tool to follow them. This is manual
context, not automatic installation or discovery. A text-only chat cannot
perform browser or runtime checks merely by receiving a skill.

## Compatibility evidence

| Route | What is supported | What has been checked here |
|---|---|---|
| Claude Code | Standard skill folder and documented CLI destination | Local CLI install and complete resource preservation; model execution recorded separately |
| Claude web/desktop | One folder per upload ZIP | Five ZIP contents, hashes and reproducibility; account upload not tested |
| Codex and other CLI destinations | Portable instructions plus agent-specific install paths | Listed paths tested locally where recorded; no claim of every-agent runtime validation |
| Other file-reading assistants | Explicit manual reading of the skill and references | No automatic loading promised |

The five entrypoints use shared Agent Skills fields, not Claude-only or
Codex-only commands. `agents/openai.yaml` is optional Codex UI metadata; other
agents can read the core without using it. Tool access and task success are
separate from installation. See the dated [cross-agent installation record](../evals/results/cross-agent-install-2026-10-03.md).

## Native Codex installer

If Codex's built-in skill-installer script exists, run it with your Python command. Python is not required to execute the prose skills; it is used by this installer and repository checks.

macOS/Linux:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo sajadjanat/iran-market-skills --path skills/iran-market-discovery skills/iran-product-benchmark skills/persian-rtl-ux skills/persian-brand-copy skills/persian-seo
```

Windows PowerShell:

```powershell
python "$env:USERPROFILE/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo sajadjanat/iran-market-skills --path skills/iran-market-discovery skills/iran-product-benchmark skills/persian-rtl-ux skills/persian-brand-copy skills/persian-seo
```

Use your actual CODEX_HOME path if configured elsewhere. An existing destination is not overwritten by this installer. Inspect it before replacing/updating; preserve local edits. Restart or start a new task as needed.

## Test local changes

From an isolated test project, point the CLI at the checkout:

```bash
npx skills@latest add /absolute/path/to/iran-market-skills --list
npx skills@latest add /absolute/path/to/iran-market-skills --skill '*' --agent codex --copy -y
```

Then inspect installed references and run relevant requests. Keep test installations out of your normal global skill directory.

For native installer testing, use a published commit with `--ref` and a temporary `--dest`. Keep tests out of your personal skills directory.

## Updates

Use `npx skills update` for CLI-managed skills; follow its project/global selection. Review local edits before updating. A plain copied skill does not auto-update. Use one installation method per skill to avoid duplicate/conflicting copies.

## Tools and packaging

For optional demo browser checks, use an isolated Python environment:

```bash
python -m pip install -r requirements-browser.txt
python -m playwright install chromium
python scripts/check_rtl_demo.py
```

On Windows an installed Edge can be selected with `--channel msedge`. These checks cover the original demonstration pages, not every platform's RTL behavior. [Recorded validation](../evals/results/review-2026-10-03.md) distinguishes actual checks from unverified behavior.

Current market/SEO claims need browsing or dated supplied sources; runtime RTL checks need browser/app access. Copywriting can run from a factual brief offline. Missing tools lead to a bounded review or plan.

Codex UI metadata and the plugin manifest are product-specific. Core skill files use the portable Agent Skills format. No marketplace listing or universal compatibility is implied.
