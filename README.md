# Iran Market Skills

Five focused Codex skills for researching Iranian product markets and building Persian digital experiences. The pack provides repeatable workflows and source guides; it is not a database of universal Iranian preferences.

## Skills

| Skill | Use it for |
|---|---|
| `iran-market-discovery` | Market opportunity, segment, competitor, and demand research for Iran |
| `iran-product-benchmark` | Dated UX comparisons of Iranian apps and websites |
| `persian-rtl-ux` | Persian localization and RTL design or implementation reviews |
| `persian-brand-copy` | Persian brand, product, and campaign copy for a defined audience |
| `persian-seo` | Technical and content SEO for Persian-language sites |

Each skill has a `SKILL.md` plus focused references. The plugin manifest groups them for Codex plugin packaging. GitHub hosting alone does not install or publish a plugin to Codex's plugin directory.

## Install individual skills

Use Codex's built-in skill installer with the public repository:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo sajadjanat/iran-market-skills \
  --path skills/iran-market-discovery \
        skills/iran-product-benchmark \
        skills/persian-rtl-ux \
        skills/persian-brand-copy \
        skills/persian-seo
```

Restart or start a new Codex task after installation so the skills are discovered.

## Evidence and scope

- Use current first-party or official sources for changing facts and cite the page used.
- Label public facts, dated observations, user-provided evidence, and hypotheses separately.
- Treat Iran as diverse by geography, age, income, language, access, and product context; do not infer a single national persona from aggregate statistics.
- Keep customer research private and de-identified. Public references point to source material; the repository does not republish third-party pages or screenshots.
- Check `DATA-POLICY.md` before adding datasets, examples, screenshots, or cultural claims.

## Sources

The source guides list official and first-party references. Their URLs and status can change; each task should verify the source again when current accuracy matters. See [`research/iran-public-sources-pilot.md`](research/iran-public-sources-pilot.md) for the source review behind this pilot.

## Status

Pilot release candidate. Source references were checked on 2026-10-03. No license file is included; the repository owner can add one before granting broader reuse rights.
