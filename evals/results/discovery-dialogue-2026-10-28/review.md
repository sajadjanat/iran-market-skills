# Discovery dialogue evaluation — 2026-10-28

Base revision: `5a09db5b4f935fbe8c33e08a40af1913db7de57b`, with the selected skill modified locally. [Package fingerprints](skill-fingerprints.json) identify the exact seven files evaluated and were matched to both isolated copies after the runs.

The owner requested an improvement after a real discovery conversation continued collecting information beyond the point of a useful recommendation. The new cases use expressly synthetic organizer data, not a published copy of the owner's customer records. The real conversation is motivation for the regression cases, not a controlled baseline or evidence of model-performance improvement.

Following the repository's fresh-session requirement, two independent Codex collaboration sessions with no inherited chat history received the selected package and one request each, in isolated temporary folders. Criteria and expected answers were withheld. Only package/request reading and output writing were permitted; browsing, other projects/skills and external actions were prohibited. The exact runtime model identifier was not exposed. The parent read both complete outputs and graded with awareness of the criteria; the review was not blinded.

| Case | Result | Actual behavior |
|---|---|---|
| [Guided clarification](market-guided-clarification.md) | 4/4 | One requester clarification about city included a provisional recommendation and data-based rationale. Concentration and unknown acquisition/return motives were retained. The two customer-facing episode prompts stayed separate and neutral. |
| [Stop intake](market-stop-intake.md) | 5/5 | Delivered an art-organizer hypothesis and bounded test without another intake question, used evidence beyond the dominant account, retained unknown sales/motivation, and placed outreach construction after discovery. Suggested criteria remained proposals with success/change/inconclusive paths. |

[Machine-readable review](results.json) preserves the nine criterion-level judgments, supporting excerpts and output hashes. These are qualitative offline passes on two supplied cases. No previous-version run, live customer interviews, outreach execution, conversion experiment or cross-model comparison was performed; the results do not establish a general reduction in question count or improved business outcomes.

Structural checks: repository validator passed, all nine existing unit tests passed, all five ZIPs built, and `git diff --check` passed with only local line-ending normalization warnings. No product/database/global-installation/hosted-download changes or release publication were performed. Source checks from the methods review were not rerun because this update adds conversation behavior rather than new external factual claims.
