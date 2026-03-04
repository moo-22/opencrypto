# Contributing to OpenCrypto

Thank you for considering a contribution to OpenCrypto! This document explains
how to set up your environment, make changes, and submit a pull request.

## Getting Started

```bash
git clone https://github.com/kayrademirkan/opencrypto.git
cd opencrypto
python -m venv .venv && source .venv/bin/activate
pip install -e ".[all,dev]"
```

## Branch Strategy

| Branch   | Purpose                        |
|----------|--------------------------------|
| `main`   | Stable release — always green  |
| `dev`    | Integration branch for PRs     |
| `feat/*` | New features or modules        |
| `fix/*`  | Bug fixes                      |

Create your branch from `main`:

```bash
git checkout -b feat/my-feature main
```

## Making Changes

1. **Write code** — follow the existing style (no trailing whitespace, 120-char
   line limit, type hints on public APIs).
2. **Add tests** — place them in `tests/` mirroring the source structure
   (e.g. `tests/test_shield_guard.py`).
3. **Run the test suite** before pushing:

```bash
pytest tests/ -v
flake8 opencrypto/ --max-line-length=120
```

4. **Update documentation** if your change adds or modifies public API.

## Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add Bollinger Band width indicator
fix: correct trailing SL calculation for SHORT positions
docs: improve DataBridge docstrings
```

## Pull Request Checklist

- [ ] Branch is up to date with `main`.
- [ ] All tests pass (`pytest tests/ -v`).
- [ ] No new linting errors (`flake8`).
- [ ] Public functions have docstrings and type hints.
- [ ] PR description explains *what* changed and *why*.

## Code Style

- **Formatting**: 4-space indentation, 120-character line limit.
- **Imports**: stdlib → third-party → local, separated by blank lines.
- **Type hints**: Required on all public function signatures.
- **Docstrings**: Google style for public APIs.
- **Logging**: Use `logging.getLogger(__name__)` — never `print()`.

## Reporting Bugs

Open a [GitHub Issue](https://github.com/kayrademirkan/opencrypto/issues) with:

1. Python version and OS.
2. Minimal reproduction steps.
3. Expected vs. actual behaviour.
4. Full traceback (if applicable).

## Security Vulnerabilities

Please **do not** open a public issue for security vulnerabilities.
See [SECURITY.md](SECURITY.md) for responsible disclosure instructions.

## License

By contributing, you agree that your contributions will be licensed under the
[MIT License](LICENSE).
