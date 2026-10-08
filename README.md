# Iran Market Skills

**Five independent skills for Iranian market research, Persian content and RTL products.**

[فارسی](README.fa.md) · [Quick start](#quick-start) · [Before & after](#before--after) · [Guides](docs/README.md) · [MIT](LICENSE)

![Conceptual illustration of five modules for research, comparison, RTL, writing and search](docs/assets/readme/hero.png)

Give your agent a concrete task, the right local context and a clear definition of done. Get a research decision, a dated comparison, an RTL review, usable Persian writing or a page-level SEO plan—with facts and unknowns kept visible.

**For developers, product teams, researchers and editors.** Persian language and Iranian geography are separate inputs; each brief keeps its own audience and voice.

## Quick start

With Node.js and Git installed, install all five through the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills@latest add sajadjanat/iran-market-skills --skill '*'
```

Choose your agent in the installer, or append `--agent codex`, `--agent claude-code` or `--agent cursor`. Check the CLI's current runtime requirements; start a fresh task if needed for discovery.

Then give a selected skill a real input:

```text
Use $persian-brand-copy to write a practical Persian article.
Read the supplied approved passages and preserve their conversational voice.
Introduce one activity, explain its materials and show a complete example round.
End with something the reader can try. Verify facts; label fictional examples.
Return a draft only.
```

For a form audit, use `$persian-rtl-ux` with [the demo source](examples/rtl/before.html). A small edit can stay a small edit.

<details>
<summary>Install one skill, inspect the list, or use Claude web/desktop</summary>

```bash
npx skills@latest add sajadjanat/iran-market-skills --list
npx skills@latest add sajadjanat/iran-market-skills --skill persian-rtl-ux --agent codex
```

For Claude web/desktop, build current per-skill ZIPs from this checkout:

```bash
python scripts/package_skills.py
```

Upload `dist/<skill-name>.zip`, not the repository ZIP or outer collection bundle. Account availability and upload/execution remain unverified here. See [installation routes](docs/installation.md) for manual installation, Windows and other agents. [Hosted downloads](https://sepehra.ir/skills/#install) have a separate publication state; updating source does not update those ZIPs.

</details>

## Choose a skill

| Your task | Skill | Useful output |
|---|---|---|
| Decide which customer need to investigate | [iran-market-discovery](docs/iran-market-discovery.md) | Evidence ledger, bounded recommendation and next experiment |
| Compare Iranian products or editorial experiences | [iran-product-benchmark](docs/iran-product-benchmark.md) | Dated observations, trade-offs and original adaptations |
| Fix Persian forms, mixed text or reading interfaces | [persian-rtl-ux](docs/persian-rtl-ux.md) | Located issues, scoped changes and actual test limits |
| Write brand copy, practical articles or tutorials | [persian-brand-copy](docs/persian-brand-copy.md) | Connected text in the approved voice, with facts checked |
| Improve pages or choose new content | [persian-seo](docs/persian-seo.md) | URL-level priorities, reader outcomes and a measurement plan |

Use one skill or combine outputs deliberately. Every package contains its own references, evidence policy and license; none requires another skill or plugin.

## Before & after

### A Persian form: direction, identifiers and focus

Actual screenshots of the repository's **synthetic demo**, captured on 2026-10-08 in headless Edge at the same 390 × 360 viewport, with identical phone input and focus state. The form has no backend.

<table>
<tr><th>Before</th><th>After</th></tr>
<tr>
<td><img src="docs/assets/readme/rtl-before.png" width="390" alt="Before: left-aligned Persian form, small unassociated phone label and default input focus"></td>
<td><img src="docs/assets/readme/rtl-after.png" width="390" alt="After: RTL form, isolated Latin order ID, labelled phone field and visible focus outline"></td>
</tr>
</table>

| Change | Why it matters |
|---|---|
| `lang="fa"`, `dir="rtl"` | Establish Persian language and reading direction |
| Isolated LTR order ID | Keep `AB-123/45` readable without rewriting its value |
| Associated label and focus style | Give the field a programmatic name and visible focus |
| Logical spacing and wrapping | Support the intended layout at narrow widths |

Inspect [before HTML](examples/rtl/before.html), [after HTML](examples/rtl/after.html), [capture details](docs/assets/readme/capture.json) and [earlier keyboard/browser verification](evals/results/review-2026-10-03.md). Appearance alone does not establish screen-reader, native keyboard, clipboard or backend behavior.

### A practical idea: from vague advice to a usable activity

An original illustrative rewrite—not a controlled with-skill/without-skill experiment:

| Vague copy | Practical rewrite for a conversational brief |
|---|---|
| «با یک فعالیت خلاقانه، لحظاتی فراموش‌نشدنی برای دوستان خود رقم بزنید.» | «یه کاغذ بذار وسط و از هر نفر بخواه یه خط به نقاشی اضافه کنه. نفر بعد باید همون شکل رو ادامه بده؛ بعد از یه دور، ببینید هر کدومتون فکر می‌کردید دارید چی می‌کشید.» |

The rewrite gives a reader an activity and a next step. A full article needs setup, a worked round and a clear ending. Formal briefs retain formal Persian. See [the article method](skills/persian-brand-copy/references/articles.md), [a full captured article](evals/results/editorial-2026-10-08/copy-practical-article.md) and [the editorial lessons](docs/editorial-lessons.fa.md).

## Useful local context

Check details that change the task: rial/toman and final cost, payment states, digit/phone contracts, selected calendar and timezone, actual service coverage, mixed-script text and Persian query intent. [The coverage map](docs/iran-context.fa.md) explains the scope.

For content, preserve approved voice, teach through concrete examples and research the reader's circumstances. One owner's taste or a few Persian search results cannot establish what all Iranians prefer. Available project evidence comes before unnecessary requests for more access.

## Evidence and status

| Record | What it establishes |
|---|---|
| [Editorial · 2026-10-08](evals/results/editorial-2026-10-08/review.md) | Five fresh sessions; 20 reviewed criteria passed on fictional inputs |
| [Operating contracts · 2026-10-04](evals/results/iran-contracts-2026-10-04/review.md) | Five cases; 21 criteria passed on synthetic data |
| [Local context · 2026-10-03](evals/results/iran-context-2026-10-03/review.md) | Five cases; 22 criteria passed on fictional inputs |
| [Source review](research/source-review-2026-10-03.md) | Dated access statuses, including unavailable sources |

Scoped checks are not a reader study, ranking guarantee or measured conversion improvement. Tool access and current facts need verification for each task. [Data policy](DATA-POLICY.md) separates observations, user evidence, inferences and hypotheses. [Real-user validation](docs/user-validation.fa.md) is still a proposed method, not a completed study.

**Release status:** `0.2.0` is Unreleased in [CHANGELOG.md](CHANGELOG.md). Source installation, hosted ZIP publication and marketplace listing are separate. The [Agent Skills format](https://agentskills.io/specification) and Codex UI metadata support discovery; discovery does not establish execution across every agent. [Claude account upload](evals/results/claude-account-check-2026-10-04.md) remains unverified.

## Development and contributions

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

Structural checks cover independent packages, metadata, links and archives. Behavioral changes need actual runs using [the evaluation protocol](evals/README.md).

Bring an anonymized input, the failure and the observable expected outcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md); use the [release checklist](docs/releasing.md) before publication and [README standard](docs/readme-standard.md) when updating this page.

**Maintainer:** [Sajad Jannat](https://github.com/sajadjanat) · [Project page](https://sepehra.ir/skills/) · [Issues](https://github.com/sajadjanat/iran-market-skills/issues)

Repository-authored material is [MIT licensed](LICENSE). Third-party sources retain their rights. [Visual provenance](docs/assets/readme/README.md) distinguishes the generated cover from actual demo captures.
