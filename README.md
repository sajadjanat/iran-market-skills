# Iran Market Skills

[فارسی](README.fa.md) · [MIT](LICENSE) · [Examples and guides](docs/README.md) · [Explore on Sepehra](https://sepehra.ir/skills/)

Five focused agent skills for researching Iranian product opportunities and building usable Persian digital products. Get a decision, a dated comparison, a concrete RTL review, usable Persian copy or a prioritized SEO audit—with evidence and unknowns visible.

## Try a concrete task

A Persian interface can look right while breaking Latin order IDs, phone inputs or keyboard labels. The RTL skill reviews these cases and distinguishes source findings from runtime checks.

See the original synthetic [before](examples/rtl/before.html) and [after](examples/rtl/after.html) pages and the [walkthrough](docs/persian-rtl-ux.md). The example demonstrates fixes; it is not a measured conversion result.

Works with standard skill loaders, including Claude Code and the Skills CLI destinations. Claude web/desktop has per-skill ZIP downloads; see [installation routes](docs/installation.md#claude-code). For a visual comparison, see [before and after on Sepehra](https://sepehra.ir/skills/#examples).

## Iranian operating details

[Persian 16-topic coverage map](docs/iran-context.fa.md): money units and final cost, payment recovery, mobile/SMS, selected calendar, address/service area, RTL, trust and local search. Relevant rules are bundled inside each independent skill; provider policies and audience behavior are not inferred.

Editorial work: [Persian article lessons and scope](docs/editorial-lessons.fa.md) cover connected articles, practical examples, situated local fit and evidence-based content decisions.

## Install

With Node.js and Git available, use the [Skills CLI](https://github.com/vercel-labs/skills). Check the current CLI's Node requirement.

```bash
npx skills@latest add sajadjanat/iran-market-skills
```

### Install the complete collection

Install all five skills in one command, then choose your agent:

```bash
npx skills@latest add sajadjanat/iran-market-skills --skill '*'
```

For a specific tool, append `--agent claude-code`, `--agent codex` or
`--agent cursor`. Start a fresh conversation/task after installation if needed.

**Claude web/desktop:** [download the complete collection ZIP](https://sepehra.ir/skills/downloads/iran-market-skills-bundle.zip).
Extract it, then upload each of the five inner ZIPs through Customize → Skills.
The collection ZIP is a download bundle, not a single Claude skill upload.
See [the guided installer](https://sepehra.ir/skills/#install) and
[upload instructions](docs/installation.md#claude-webdesktop-claudeai).
Account upload remains independently untested.

### Install an individual skill

To inspect the collection or target one skill:

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

0.2.0 is a release candidate; publication status is recorded in [CHANGELOG.md](CHANGELOG.md). See [actual validation results](evals/results/review-2026-10-03.md) for package installation, behavioral scenarios and browser/hosted CI checks. The Codex plugin manifest packages the collection; it does not itself publish to a marketplace.

See [contributing](CONTRIBUTING.md) and [release/maintenance checks](docs/releasing.md). Repository-authored material is MIT licensed; linked third-party sources retain their own rights.

Persian language and the Iranian market are separate inputs. The [Iran-context review](research/iran-context-review-2026-10-03.md) informs local customer interviews, transaction-state copy, digit-entry contracts and truthful local/seasonal pages; these recommendations still need validation with the intended users.

A [Persian real-user validation guide](docs/user-validation.fa.md) defines practical comprehension/task checks; no such customer study has been run in this repository.

The [five fresh local-context evaluations](evals/results/iran-context-2026-10-03/review.md) passed their 22 criteria. Their fictional inputs and limits are recorded; this is not a customer study.

The [2026-10-04 contract evaluation](evals/results/iran-contracts-2026-10-04/review.md)
records five fresh-session outputs and 21 passing criteria on synthetic inputs.
[Claude account validation](evals/results/claude-account-check-2026-10-04.md)
remains unverified after the available browser reached sign-in.
