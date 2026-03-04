# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.x     | Yes       |

## Reporting a Vulnerability

If you discover a security vulnerability in OpenCrypto, **please do not open a
public GitHub issue.** Instead, report it privately so we can address it before
public disclosure.

### How to Report

Send an email to **kayrademirkan@proton.me** with the following information:

1. **Description** of the vulnerability.
2. **Steps to reproduce** or a proof-of-concept.
3. **Impact assessment** — what an attacker could achieve.
4. **Suggested fix** (optional, but appreciated).

### What to Expect

- **Acknowledgement** within 48 hours.
- **Status update** within 7 days with an estimated fix timeline.
- **Credit** in the release notes (unless you prefer to remain anonymous).

### Scope

The following are in scope:

- Secret leakage (API keys, tokens exposed through framework behaviour).
- Injection vulnerabilities in data processing pipelines.
- Dependency vulnerabilities that affect OpenCrypto users.
- Unsafe deserialization of trade history or configuration files.

### Out of Scope

- Vulnerabilities in third-party services (Binance API, Telegram, Groq).
- Issues requiring physical access to the host machine.
- Social engineering attacks.

## Security Best Practices for Users

- **Never commit `.env` files** to version control.
- Keep dependencies up to date: `pip install --upgrade opencrypto`.
- Use environment variables or a secrets manager for all API keys.
- Run the framework in an isolated environment (venv / container).
