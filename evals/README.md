# Behavioral evaluation protocol

[cases.json](cases.json) contains realistic requests and observable criteria for all five skills. Fixtures are repository-authored synthetic data. They are not market studies or live-site observations.

## Run a case

1. Use a fresh agent session with only the selected skill package and the listed input fixtures. Keep output in an isolated workspace. Supply the case request without the grading criteria.
2. Record date, repository revision/working-tree state, agent/model, available tools and whether browsing/runtime access was allowed. State model version unavailable if not exposed.
3. Keep the actual output. A reviewer checks each criterion and records pass/fail/unverified with the supporting excerpt or artifact.
4. A failed material criterion fails the case. An unverified criterion remains unverified; do not count it as passed.
5. Correct demonstrated failures and rerun the affected scenario. Use the same inputs when comparing changes.

Structural validation checks case coverage and fixture existence. It does not execute model evaluations. Record actual runs in `evals/results/`; do not present expected outputs as measured results.

## Comparison protocol

For an optional with-skill/without-skill comparison, use the same model, user request, tools and artifacts in fresh sessions. Compare task completion, factual support, handling of missing evidence and practical usability. Do not claim performance or conversion improvements from a single example.

The [packaging validator](../scripts/validate_repo.py) and [regression checks](../tests/test_validation.py) provide offline checks separate from this protocol.

The [2026-10-03 local-context run](results/iran-context-2026-10-03/review.md) uses five fresh sessions, one per new case, with isolated outputs and separate package fingerprints. It supplements the earlier grouped pilot; it does not replace its historical record.

The [2026-10-04 operating-contract run](results/iran-contracts-2026-10-04/review.md)
records the five newer contract cases with exact outputs, criterion-level
evidence and package fingerprints. Claude account validation remains
[unverified after a sign-in redirect](results/claude-account-check-2026-10-04.md).

The [2026-10-08 editorial run](results/editorial-2026-10-08/review.md) records five fresh-session offline cases, exact package/output hashes, criterion-level evidence and audience/runtime limitations.
