# Discovery methods evaluation — 2026-10-26

Base revision: `90cd734a7e961a6de495b6b15e3750ab665f8589`; evaluated with the discovery package modified in the working tree. [Package fingerprints](skill-fingerprints.json) identify the exact seven files and were matched to all three isolated evaluation copies after execution.

The repository requires fresh-session behavioral checks for workflow changes. Three Codex collaboration agents with no inherited conversation each received one request and only the selected skill package in separate temporary directories. Criteria, report synthesis, intended answers and repository history were withheld. Local selected-package reading and output writing were permitted; browsing, other projects/skills, contacting people and other external actions were prohibited. The exact runtime model identifier was not exposed. Synthetic status is part of the two new requests; the existing offline case explicitly supplies no customer/category evidence.

The parent read the complete outputs and reviewed each criterion. The reviewer knew the criteria and was not blinded. [Results and verbatim excerpts](results.json) record all 14 scoped criteria as passed:

| Case / preserved output | Result | Observed behavior |
|---|---|---|
| [No market evidence](market-offline.md) | 4/4 | Bounded segment decision, hypotheses rather than invented market figures, recruiting plan and explicitly proposed criteria. |
| [Interest versus payment](market-interest-vs-payment.md) | 5/5 | Unknown transactions were not changed to zero; event ratios were not treated as unique-user conversion; price statements and compliments did not validate price; bounded next checks and inconclusive outcomes were retained. |
| [Interviews and switching](market-interview-and-switching.md) | 5/5 | Annual/monthly buying cycles changed recall windows; phone/manual alternatives remained relevant; unsupported guarantee uplift and WTP coefficient were rejected; MVP remained conditional rather than forbidden. |

No previous-version/without-skill comparison was run. These qualitative offline examples do not establish improved model performance, representative Iranian demand, customer outcomes, profitable pricing or cross-agent compatibility. No interview, participant observation, actual transaction or live experiment was performed. A passing case covers only its stated criteria, not every possible task.

## Structural and installation checks

- `python scripts/validate_repo.py`: passed after all documentation/evaluation files were present.
- `python -m unittest discover -s tests -v`: all 9 existing checks passed.
- `python scripts/package_skills.py`: built all 5 self-contained ZIPs; contents/reproducibility are covered by existing archive tests.
- Isolated project installation of only `iran-market-discovery` through Skills CLI 1.7.4 completed; every installed file matched the package SHA-256 manifest. No global installation was changed. The configured npm mirror first returned HTTP 402; a per-command official-registry override succeeded without changing npm configuration. CLI warned that Node 22.18.0 is below its declared >=22.20.0 requirement, so this successful copy does not establish supported runtime compatibility.
- The generic skill-creator `quick_validate.py` reported the package's pre-existing `compatibility` frontmatter unsupported. That field is supported by this repository's validator and was preserved. This generic check is not recorded as passed.
- `git diff --check`: passed; Git emitted local CRLF-to-LF normalization warnings.

This record describes source and local-package validation, not a GitHub release, marketplace publication, hosted-download refresh or real-customer study. GitHub commit/publication state is reported separately after the push.
