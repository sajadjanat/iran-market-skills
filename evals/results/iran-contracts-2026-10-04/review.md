# Iranian operating contracts — 2026-10-04

Base: `120b3b33086681e1863a6d2c6f57c0bf489103f5`. The five skill packages were
unchanged; documentation and this evaluation record were being updated.
[File fingerprints](skill-fingerprints.json) identify the exact packages read.

Five fresh Codex collaboration sessions, each with no inherited history,
received only its selected skill package, the case request and the synthetic
`iran-operating-contracts.json` fixture in an isolated temporary directory.
Agents were instructed not to read criteria, other skills or repository data.
They could read/write local files; browsing, a product browser and backend
execution were unavailable. Exact runtime model/version was not exposed.
This is not a Claude run or an every-agent compatibility result.

The parent preserved output text (published line endings normalized to LF) and reviewed it against all criteria in
`evals/cases.json`. This reviewer knew the criteria and was not blinded.
[Machine-readable results](results.json) give criterion-level evidence and
published and original captured output hashes. Skill fingerprints and the
fixture hash refer to the actual evaluated working-copy bytes. All 21 criteria passed in these five fictional cases:

| Case / actual output | Result | Evidence |
|---|---|---|
| [RTL contracts](rtl-iran-contracts.md) | 5/5 | 250000 toman goods and 280000 total; fractional policy unresolved; phone/OTP strings preserved; date-only separated from an instant; pending payment and runtime/backend unknowns retained. |
| [Persian copy](copy-iran-contracts.md) | 4/4 | Itemized 280000 total; 72-hour recovery scoped to fixture's verified failure and source account; pending/OTP/service-area messages add no unsupported promises. |
| [Product benchmark](benchmark-iran-contracts.md) | 4/4 | B's original 2800000 rial becomes 280000 toman; A's final cost remains unknown; no overall cheapest winner or fabricated live interaction. |
| [Market discovery](market-iran-contracts.md) | 4/4 | Four explicit hypotheses, recent-experience interviews in Shiraz, relevant cost/SMS/alternative questions and no national demand or trust inference. |
| [Persian SEO](seo-iran-contracts.md) | 4/4 | IRR price corrected to 2500000; local date display separated from machine format; unsupported city/spelling pages rejected; live policy/indexing/traffic remain unverified. |

No material criterion failure was demonstrated, so this run does not justify
rewriting the skill workflows. It is a scoped qualitative check, without a
no-skill baseline, statistical estimate, user study or real payment evidence.
It does not measure conversion, real SMS delivery, gateway behavior, native
keyboard/accessibility support or Claude execution.

Other validation: the packaging validator and nine regression tests passed.
The live collection ZIP was downloaded; all five inner ZIP hashes matched
its manifest. No skill resources changed, so previous public packages remain
valid. [Claude account access](../claude-account-check-2026-10-04.md) reached
sign-in, leaving actual upload and Claude output quality unverified.
