# Release and maintenance checklist

A release is ready only when its checks are recorded. An Unreleased changelog entry is not a publication claim.

1. Check the diff and intended version in the plugin manifest and changelog. Keep release scope at five skills.
2. Install dev dependencies, synchronize canonical resources and run offline validation plus regression checks.
3. From an isolated project, point the CLI at the checkout as shown in the installation guide; list and copy-install the skills, then inspect packaged references. Check the CLI's current Node requirements.
4. Run relevant [behavioral cases](../evals/README.md), recording model/version/tools, actual outputs, criteria and gaps. For RTL changes, perform applicable browser/mobile/keyboard checks, not only a source review.
5. Reopen references for changed or volatile claims. Update [source review](../research/source-review-2026-10-03.md) or add a new dated review. Keep inaccessible sources visibly pending.
6. Confirm English/Persian docs and UI prompts match the packaged behavior. Check the [MIT license](../LICENSE) and third-party evidence boundaries.
7. Record release date and results only after checks finish. Commit/review/publish according to the owner's chosen workflow. A plugin manifest does not submit to any marketplace.

## Maintenance cadence

Review changing sources before using them; inspect key references at each release and after reported redirects/policy changes. Rerun affected behavioral cases after workflow changes. Treat a link returning 200 as access evidence only, not content verification. Record agent compatibility separately from skill discovery.

No scheduled automation is created by this document.
