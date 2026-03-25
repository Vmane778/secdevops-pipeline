# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please **do not** open a public GitHub issue. Instead:

1. **Email** the security team with:
   - Description of the vulnerability
   - Steps to reproduce (if applicable)
   - Potential impact
   - Affected version(s)

2. **Response Timeline**:
   - Initial acknowledgment: Within 48 hours
   - Status update: Within 7 days
   - Resolution target: Based on severity

## Security Practices

### Automated Security Measures

- **Container Scanning**: Every Docker image is scanned with Trivy during CI/CD pipeline
- **Code Linting**: Python code is checked with flake8 for common issues
- **Dependency Monitoring**: Regular checks for vulnerable dependencies
- **Vulnerability Reporting**: Results uploaded to GitHub Security tab

### Security Updates

- Critical vulnerabilities: Patched immediately
- High vulnerabilities: Patched within 7 days
- Medium vulnerabilities: Patched within 30 days
- Low vulnerabilities: Addressed in next release

### Best Practices

- Keep dependencies updated via Dependabot
- Use secrets management for sensitive data
- Review security scan results regularly
- Follow secure coding practices

## Dependencies

Current dependencies are managed in `requirements.txt`. Security advisories for known vulnerabilities in dependencies are checked automatically.
