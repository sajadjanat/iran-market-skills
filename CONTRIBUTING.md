# Contributing

Start with a concrete request the existing skill handles poorly. Include an anonymized input and the observable expected behavior. This release concentrates on completing the five existing skills.

## Edit and check

1. Update the skill entrypoint and the relevant conditional reference.
2. Keep its UI metadata and human guide consistent. Preserve automatic invocation.
3. Add or update behavioral cases for the changed decision.
4. After editing the canonical policy or license, run `python scripts/sync_resources.py`.
5. Install development dependencies with `python -m pip install -r requirements-dev.txt`.
6. Run `python scripts/validate_repo.py` and `python -m unittest discover -s tests -v`.
7. Run affected behavioral scenarios following [the evaluation protocol](evals/README.md), recording model/tools, output, pass/fail and limitations.

The offline validator checks packaging and metadata, not external URL availability or output quality. Do not rewrite tests merely to make a broken skill pass. Keep each skill's local references inside its package.

## Evidence and rights

Apply [DATA-POLICY.md](DATA-POLICY.md). Record original publisher, exact URL, source date, access date/status and claim scope. If inaccessible, mark it pending. Label synthetic examples; publish no personal customer data or third-party assets without suitable rights. New contributions are provided under the repository's [MIT license](LICENSE).

## Changes and releases

Describe behavioral changes in [CHANGELOG.md](CHANGELOG.md). Follow [the release checklist](docs/releasing.md) before changing the release state or making compatibility claims.
