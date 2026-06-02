# AGENTS.md

## Project Overview

`openwisp-docs` contains the OpenWISP documentation published on openwisp.io.

Core content lives in this repository root:

- `modules/`, `user/`, `developer/`, `general/`, `tutorials/`, `releases/`, and top-level `.rst` files contain documentation content.
- `_static/`, `_templates/`, `_styles/`, `assets/`, `images/`, and `partials/` contain presentation assets and shared snippets.
- `conf.py`, `config.yml`, `build.py`, `Makefile`, and helper scripts support documentation builds and releases.

## Source of Truth

- Use `README.rst` and `developer/contributing.rst` for setup, style, and contribution guidance.
- Use `.github/workflows/ci.yml`, `pyproject.toml`, and `requirements.txt` for CI-tested docs build, QA, spelling, and link checks.
- Use GitHub issue/PR templates when asked to open issues or PRs.

If instructions conflict, repository config and CI workflows win first, docs next, and this file is supplemental.

## Development Notes

- Keep changes focused. Avoid unrelated rewrites, formatting churn, and broad style changes.
- Preserve headings, anchors, cross-references, versioned links, include directives, image paths, and public URLs unless explicitly required.
- Be careful with release notes, version switcher behavior, generated files, spell-check word lists, and module documentation copied from upstream repos.
- Avoid unnecessary blank lines inside directive blocks, literal blocks, and helper functions.
- Update navigation and index files when adding, moving, or removing pages.

## Testing and QA

- Add or update docs examples and references for behavior changes.
- For documentation bug fixes, reproduce the broken build, link, warning, or rendered output when feasible before changing it.
- Use targeted docs builds while iterating, then run the documented full QA/build command before considering the change complete.
- Run `./run-qa-checks` when present. Treat failures as blocking unless confirmed unrelated and reported.

## Security Notes

- Watch for leaked secrets, unsafe links, stale security guidance, broken HTTPS links, and instructions that encourage insecure deployments.
- Preserve safe handling around downloads, install commands, credentials, tokens, TLS material, and production configuration examples.
- Write comments only when they explain why code or docs structure is shaped a certain way. Put comments before the relevant block instead of scattering them inside it.

## Troubleshooting

- If setup, QA, spelling, links, or docs builds fail, check docs first, then compare with CI. If commands diverge, follow CI.
