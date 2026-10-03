# Installation and compatibility

## Skills CLI

Requires Git and Node satisfying the current [CLI package](https://github.com/vercel-labs/skills). CLI discovery of the five packages has been checked; it is separate from executing every skill on every agent.

```bash
npx skills@latest add sajadjanat/iran-market-skills
npx skills@latest add sajadjanat/iran-market-skills --skill persian-rtl-ux --agent codex
npx skills@latest add sajadjanat/iran-market-skills --list
```

On PowerShell, use `npx.cmd` if execution policy blocks the npm PowerShell wrapper. Copy mode can be useful when symlinks are unavailable.

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

For native installer testing against a prepared branch, use `--ref improve-five-skills` and a temporary `--dest` after the branch is available remotely. Public main does not contain unmerged changes.

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
