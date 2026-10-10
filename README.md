# Iran Market Skills

**Five skills for taking an Iranian or Persian product from an open question to work you can review, use and test.**

[فارسی](README.fa.md) · [Start](#start) · [Five work situations](#five-work-situations) · [Evidence](#evidence-and-project-status) · [Guides](docs/README.md) · [MIT](LICENSE)

![Conceptual illustration of research, comparison, Persian interfaces, writing and search](docs/assets/readme/hero.png)

You are considering a product, choosing a booking flow, fixing an invoice screen, explaining a feature or deciding which pages to improve. Each task needs a different kind of work. This collection gives your AI agent a method for doing that work and a concrete definition of what to deliver.

The result might be a decision memo, an annotated comparison, a code patch with checks, a complete Persian help article or a prioritized list of page changes. **The useful question is: what will I have in my hands when this task is finished?**

A skill contains instructions and references your agent reads while working. The agent provides the model and tools; you provide the project, facts and authorized access. Each of the five packages works independently. They are intended for founders, product teams, developers and editors working on Iranian services or Persian experiences.

## Start

With Node.js and Git available, install the collection through the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills@latest add sajadjanat/iran-market-skills --skill '*'
```

Select your agent in the installer, or add `--agent codex`, `--agent claude-code` or `--agent cursor`. See [installation](docs/installation.md) for runtime requirements and manual routes.

Try this self-contained fictional brief:

```text
Use $persian-brand-copy to write a short Persian help article.
Fictional product facts: in «مخاطبان», the user can optionally filter by
«برچسب», then select «خروجی CSV». The file contains only contacts in the
current selection. An empty selection shows «مخاطبی برای خروجی وجود ندارد».
Use a clear, friendly voice. Give a title, steps, a worked example and
empty-state guidance. Preserve those exact UI labels. Return a draft.
```

The deliverable is a help article someone can follow from opening the page to recognizing the result. All required facts are in the request; no repository fixture is needed. Replace them with your actual interface facts for production work.

<details>
<summary>Install one skill, list the collection, or build uploadable packages</summary>

```bash
npx skills@latest add sajadjanat/iran-market-skills --list
npx skills@latest add sajadjanat/iran-market-skills --skill persian-rtl-ux --agent codex
```

For Claude web/desktop, generate independent ZIPs from a checkout:

```bash
python scripts/package_skills.py
```

Upload the relevant `dist/<skill-name>.zip`. Account upload and execution remain unverified here. The [installation guide](docs/installation.md) covers Windows and other agents. [Hosted downloads](https://sepehra.ir/skills/#install) have a separate publication state from source changes.

</details>

## Choose by the work you need to finish

| Your situation | Skill | What you receive |
|---|---|---|
| You need to decide what to investigate before building | [iran-market-discovery](docs/iran-market-discovery.md) | Decision memo, evidence gaps and a validation plan |
| You need to choose an interaction or content pattern | [iran-product-benchmark](docs/iran-product-benchmark.md) | Task comparison, annotated observations and design recommendations |
| Your Persian interface needs an audit or implementation | [persian-rtl-ux](docs/persian-rtl-ux.md) | Located findings or a patch, input cases and verification results |
| Your reader needs to understand an offer or complete a task | [persian-brand-copy](docs/persian-brand-copy.md) | Finished copy, article or tutorial in the requested voice |
| You need to choose which page or content task to improve first | [persian-seo](docs/persian-seo.md) | URL-level priorities, evidence, fixes and a measurement plan |

## Five work situations

**All five scenarios and output excerpts below are newly authored fictional illustrations.** They show the intended shape of a deliverable, not captured agent runs, customer results or a measured comparison with and without skills. Actual project evidence is linked separately below.

### 1. Before building an inventory tool, understand the job

You want to build an inventory tool for independent clothing shops in Rasht. You need to decide whether the first version should focus on recording stock or reconciling online and in-store sales.

**Provide:** the proposed customer and city, the decision, known constraints and any interviews, support records or dated sources you have.

```text
Use $iran-market-discovery for this fictional inventory-tool idea.
Compare stock recording and sales reconciliation as first-version
hypotheses for independent clothing shops in Rasht. We have no interviews.
Return a decision memo, what evidence is missing, neutral questions about
recent stock discrepancies and a small test to agree before development.
```

**An illustrative part of the memo:**

| Question | Evidence to collect | Decision it informs |
|---|---|---|
| What happened during the last stock discrepancy? | Reconstruct the shop's actual sequence, tools and resolution | Which job the first version should address |
| Where did online and in-store records diverge? | Inspect an authorized, anonymized example with the owner | Whether reconciliation is a real problem for that shop |
| Will the proposed workflow fit daily work? | Have a participant use a simple prototype on a sample task | Continue, change the workflow or investigate another job |

**Before → after:** a feature list becomes a set of hypotheses, questions and a test you can run. With relevant evidence, the skill can make a bounded recommendation; with this brief, the honest deliverable is a research plan. It also covers segments, alternatives, price/access constraints and situated audience research for content.

### 2. Choose a booking flow by comparing the same task

You are designing mobile booking for a rehearsal studio. Two supplied page descriptions show different ways of helping a musician choose a room and time.

**Fictional inputs:** A displays available time slots before asking for a phone number. B requests phone verification before revealing availability. Only descriptions are available.

```text
Use $iran-product-benchmark to compare these fictional mobile flows.
Task: find an available rehearsal room and time. A shows slots before
phone entry; B requires phone verification first. Return an observation
matrix, trade-offs and a recommendation for our prototype. Mark unseen
states and identify what a user test should check.
```

**An illustrative comparison:**

| Observable difference | Design implication | Next check |
|---|---|---|
| A exposes availability before phone entry | A visitor can inspect whether a suitable time exists before identifying themselves | Can they find and correctly interpret a suitable slot? |
| B places verification before availability | A visitor must complete an extra prerequisite to inspect times | What product requirement justifies that prerequisite? |
| Neither description shows final confirmation | Confirmation behavior is unknown | Inspect or request that state before evaluating booking completion |

**Before → after:** “make ours like A” becomes a reasoned prototype choice with a condition to verify. The complete report can include dated flow observations, costs and conditions, recovery states and original recommendations. The same method can compare articles and tutorials answering one reader question.

### 3. Make a Persian invoice readable without corrupting its data

Your invoice screen combines Persian descriptions, Latin reference IDs and prices. A developer needs an exact patch target and cases to verify.

**Fictional contract:** a stored value of `12500000` rial displays as `1,250,000` toman. Reference `INV-204/A` must keep its exact value. The recipient's Persian name wraps on a narrow screen.

```text
Use $persian-rtl-ux to review the supplied invoice component.
Store amounts in rial and display toman under the stated contract.
Preserve INV-204/A and the original recipient name. Check mixed text,
wrapping, logical spacing and keyboard focus. Return located changes
and actual checks; name runtime checks you could not perform.
```

**An illustrative acceptance checklist:**

| Case | Expected result |
|---|---|
| Amount `12500000` rial | Visible `۱٬۲۵۰٬۰۰۰ تومان`; original stored amount preserved |
| Reference `INV-204/A` in Persian text | Readable isolated direction; unchanged underlying string |
| Long recipient name at the target mobile width | Meaningful text remains available without horizontal overflow |
| Keyboard navigation | Controls receive focus in meaningful order and focus stays visible |

**Before → after:** “the invoice looks wrong” becomes located issues, a scoped patch and observable checks. Provide the actual component for implementation; a screenshot supports only the visible state. The skill also covers phone/OTP inputs, selected calendars/timezones, transaction states, cards and reading interfaces.

### 4. Explain a feature through a task the reader can complete

Your contact manager can export a filtered selection. The feature needs a Persian help article that makes the resulting file understandable.

**Provide:** actual UI labels and states, what the export contains, the reader's task and approved voice samples. The fictional facts in the starting request above are enough for this example.

**An illustrative Persian excerpt:**

> ‏برای گرفتن فایل یک گروه، در «مخاطبان» برچسب همان گروه را انتخاب کنید و بعد «خروجی CSV» را بزنید. مثلاً با انتخاب برچسب «همکاران»، فایل فقط مخاطبان همان انتخاب را در بر می‌گیرد. اگر «مخاطبی برای خروجی وجود ندارد» را دیدید، انتخاب فعلی خالی است؛ برچسب انتخاب‌شده را بررسی کنید.

**Before → after:** “export your contacts easily” becomes a named path, a concrete example and guidance for an empty result. The full deliverable includes a title, connected explanation, steps and verification notes for missing facts.

`persian-brand-copy` also writes landing pages, campaigns, product descriptions, interface messages and practical articles. The requested channel and brand voice determine the style. Real tutorials need real labels and states; a creative activity needs a complete example the reader can try.

### 5. Decide which store page needs attention first

A fictional coffee-equipment store has a category at `/grinders` and a guide at `/blog/choose-a-grinder`. The supplied category HTML contains `noindex`; the owner says the category should be publicly discoverable. The guide has no link to the category. Search performance data is unavailable.

```text
Use $persian-seo to prioritize this fictional page review.
The public /grinders category has noindex in supplied HTML.
/blog/choose-a-grinder has no link to that category. We have no response
headers or search-performance data. Return URL-level findings, the
next checks and a measurement plan. Assess whether another article
would add value before proposing it.
```

**An illustrative work list:**

| Priority / URL | Evidence and action | Verification |
|---|---|---|
| 1 · `/grinders` | Supplied noindex conflicts with the owner's stated intent; confirm full directive context and change if authorized | Check live headers and rendered directives; engine index status needs engine evidence |
| 2 · `/blog/choose-a-grinder` | The supplied guide has no category link; add a useful link at the relevant selection step if it fits the text | Verify the destination and rendered link |
| Next content decision | Read the existing guide and identify a distinct unanswered reader question | Use actual query or reader evidence when available |

**Before → after:** an open-ended request for more articles becomes a specific sequence of checks and page changes. The skill also covers Persian query variants, truthful local pages, content overlap and comparable measurement periods. This brief supports no traffic forecast or claim about current indexing.

## What makes the local context useful?

The details change the work: the unit attached to an amount, what a payment status really means, accepted phone/code formats, a date's calendar and timezone, actual service coverage and mixed Persian/Latin text. In content, approved register, reader circumstances and Persian query wording matter too.

Language, region and operating rules are separate inputs. A Persian interface for users outside Iran retains its own currency, calendar and service conditions. The [Iranian context map](docs/iran-context.fa.md) describes the coverage; the [data policy](DATA-POLICY.md) explains how observations, user evidence and hypotheses stay distinguishable.

Use one skill for a small task. For a larger product, a discovery memo can inform a benchmark; its recommendations can become UX and copy work; SEO can prioritize search-facing pages. Share the relevant outputs and project facts between tasks.

## Evidence and project status

The examples above are illustrations. The repository also preserves separate records:

| Record | What it supports |
|---|---|
| [Eventbaz case study](docs/use-case-eventbaz.fa.md) · Persian | A historical workspace report records copy and SEO skills used alongside project guidance to revise 11 articles; individual skill impact was not measured |
| [Editorial evaluation](evals/results/editorial-2026-10-08/review.md) | Five fresh sessions; 20 scoped criteria passed on fictional inputs |
| [Operating-contract evaluation](evals/results/iran-contracts-2026-10-04/review.md) | Five cases; 21 scoped criteria passed on synthetic inputs |
| [RTL browser verification](evals/results/review-2026-10-03.md) | Narrow demo checks in the recorded browser and widths; broader product/runtime coverage is unverified |
| [Source access review](research/source-review-2026-10-03.md) | Dated access and source limitations |

These records establish their stated scope. Reader studies, controlled skill-improvement measurements and business gains remain unmeasured. The new README scenarios have not been run as evaluations. See [evaluation methods](evals/README.md) and the [proposed real-user pilot](docs/user-validation.fa.md).

**Release:** `0.2.0` remains Unreleased in [CHANGELOG.md](CHANGELOG.md). Source installation, hosted ZIP publication and marketplace listing are separate. Agent discovery/installation does not establish successful execution in every agent; [Claude account upload](evals/results/claude-account-check-2026-10-04.md) remains unverified.

## Development and contributions

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

Structural checks cover packages, metadata, links and archives. Workflow changes also need recorded behavioral runs. To contribute, bring an anonymized brief, the observed failure and the expected deliverable. See [contributing](CONTRIBUTING.md), [release checks](docs/releasing.md) and the [README standard](docs/readme-standard.md).

**Maintainer:** [Sajad Jannat](https://github.com/sajadjanat) · [Project page](https://sepehra.ir/skills/) · [Issues](https://github.com/sajadjanat/iran-market-skills/issues)

Repository-authored material is [MIT licensed](LICENSE). Third-party sources retain their rights. The cover is a generated conceptual illustration; [visual provenance](docs/assets/readme/README.md) records its origin.
