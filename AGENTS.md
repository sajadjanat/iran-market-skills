# Maintaining Iran Market Skills

Keep the five existing skills independently installable: local links and runtime resources stay inside each skill. Human installation, contribution and release guides belong at the root or in docs.

Write discriminating descriptions, task-specific steps, observable completion criteria and honest fallbacks. Put conditional detail in linked references. Preserve the user's audience, platform, voice and requested scope. Automatic invocation remains enabled; no other skill or plugin is required.

DATA-POLICY.md and LICENSE are canonical. Run `python scripts/sync_resources.py` after changing either; it bundles identical copies into each installable skill. Do not hand-edit generated copies.

When changing a skill, update its human guide, relevant evaluation scenarios and UI metadata. Keep English/Persian installation instructions consistent. Label fictional examples and record sources' actual access status.

Run `python scripts/validate_repo.py` and `python -m unittest discover -s tests -v`. For workflow changes, run affected scenarios using evals/README.md; structural checks do not establish model quality. Record actual outcomes and limitations.

Follow docs/releasing.md before release. Plugin packaging is not marketplace publication. Never claim unsupported compatibility, fabricated performance, ranking guarantees or customer evidence. Keep changes within the requested five-skill scope.
