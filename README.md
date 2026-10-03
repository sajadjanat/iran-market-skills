# Iran Market Skills

[فارسی](README.fa.md) · [MIT](LICENSE) · [Examples and guides](docs/README.md)

Five focused agent skills for researching Iranian product opportunities and building usable Persian digital products. Get a decision, a dated comparison, a concrete RTL review, usable Persian copy or a prioritized SEO audit—with evidence and unknowns visible.

## Try a concrete task

A Persian interface can look right while breaking Latin order IDs, phone inputs or keyboard labels. The RTL skill reviews these cases and distinguishes source findings from runtime checks.

See the original synthetic [before](examples/rtl/before.html) and [after](examples/rtl/after.html) pages and the [walkthrough](docs/persian-rtl-ux.md). The example demonstrates fixes; it is not a measured conversion result.

## Install

With Node.js and Git available, use the [Skills CLI](https://github.com/vercel-labs/skills). Check the current CLI's Node requirement.

```bash
npx skills@latest add sajadjanat/iran-market-skills
```

Choose the skills and agent during installation. To inspect the collection or target one skill:

```bash
npx skills@latest add sajadjanat/iran-market-skills --list
npx skills@latest add sajadjanat/iran-market-skills --skill persian-rtl-ux --agent codex
```

Restart/start a new agent task if discovery requires it. For the native Codex installer, Windows instructions, local development and updates, see [installation](docs/installation.md). Each skill contains its own references, evidence policy and MIT license.

### First request

```text
Use $persian-rtl-ux to audit this Persian form.
Check mixed Persian/Latin text, phone inputs, labels and responsive layout.
Preserve stored identifiers. Report the checks you actually ran and what remains untested.
```

For the included demo, attach examples/rtl/before.html. If you only provide source, expect a source review—not a runtime verification claim.

## Choose a skill

| Skill | Use it for | Result / guide |
|---|---|---|
| iran-market-discovery | Decide what customer/opportunity to investigate in Iran | Evidence ledger and next experiment · [guide](docs/iran-market-discovery.md) |
| iran-product-benchmark | Compare local product flows for a specific task | Dated observations and design implications · [guide](docs/iran-product-benchmark.md) |
| persian-rtl-ux | Build or review Persian/mixed-direction UI | Scoped audit or patch and test record · [guide](docs/persian-rtl-ux.md) |
| persian-brand-copy | Write Persian copy for an audience/offer/channel | Usable copy with factual claims checked · [guide](docs/persian-brand-copy.md) |
| persian-seo | Prioritize search improvements for Persian pages | URL-level findings and measurement plan · [guide](docs/persian-seo.md) |

Use them individually. A larger product workflow can move from discovery to benchmark, then UX/copy and SEO when those tasks are relevant; no skill silently invokes another.

## Evidence and tool limits

Changing facts require current sources or dated supplied evidence. Public statistics, live observations, user evidence, inference and hypotheses are separate. Lack of browsing, login, analytics or runtime access is reported rather than filled with invented facts. Private research stays de-identified.

Sources were reviewed on 2026-10-03 with individual access statuses, including blocked/unavailable sources. See the [review](research/source-review-2026-10-03.md) and [data policy](DATA-POLICY.md). The earlier [pilot note](research/iran-public-sources-pilot.md) is historical context, not a current dataset.

## Validation and compatibility

The core packages use the [Agent Skills format](https://agentskills.io/specification); `agents/openai.yaml` provides Codex UI metadata. The CLI can discover all five. Agent-specific execution and tool support still need their own checks; discovery alone is not a compatibility guarantee.

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

Offline checks validate packaging, metadata and links. [Behavioral scenarios](evals/README.md) cover task outcomes; they require actual model runs and honest result records.

## Status and contributing

0.2.0 is prepared in the working tree; publication status is recorded in [CHANGELOG.md](CHANGELOG.md). The Codex plugin manifest packages the collection; it does not itself publish to a marketplace.

See [contributing](CONTRIBUTING.md) and [release/maintenance checks](docs/releasing.md). Repository-authored material is MIT licensed; linked third-party sources retain their own rights.
