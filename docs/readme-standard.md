# README maintenance standard

This is the project-specific contract for `README.md` and `README.fa.md`. Keep detailed installation instructions in [installation.md](installation.md) and runtime guidance inside each independent skill.

## Reading order

1. Name, one-sentence purpose, language switch and useful navigation.
2. A lightweight cover with meaningful alt text, followed by audience and concrete outputs.
3. One primary install command and a usable first request. Put alternatives in a details block.
4. A task-to-skill table with all five exact names and guides.
5. Before/after demonstrations with inputs, capture conditions, provenance and limits.
6. Local-context value, linked evidence and accurate release/compatibility status.
7. Developer checks, contribution route, maintainer and license.

Adapt prose naturally between languages; keep commands, skill names, installation routes, evidence claims and status equivalent. Avoid a blanket RTL HTML wrapper around Markdown: it can prevent tables and code blocks from rendering correctly. Use short paragraphs and descriptive links instead of repeated status appendices.

## Visuals and examples

- Store README assets in `docs/assets/readme/`; use relative paths from each consuming file.
- Label generated art in the asset record. It must not substitute for execution evidence.
- Capture comparisons from unchanged fixtures, with matching viewport, data and interaction state. Record browser, date, scale and limitations.
- Keep essential instructions in text and provide meaningful image alt text.
- Check paired images at normal GitHub width. Do not depend on external fonts, scripts or custom CSS.
- Label authored rewrites and fictional examples. A crafted before/after is not measured model improvement.
- Keep images modest in size; preserve screenshot text and record third-party rights when relevant.

## Verification before merging

Run the repository validator, existing regression checks and `git diff --check`. Check Markdown/HTML image and link targets, navigation fragments, matching installation code blocks and all five skill names in both languages. Inspect images at their displayed size. Do not add tests that enforce exact wording.

Keep dated evaluation claims linked to original records. Packaging success does not prove audience quality, compatibility or growth. README edits do not publish a release, hosted ZIP or marketplace listing. New volatile product instructions need current primary sources; keep detailed compatibility notes in their existing guides.
