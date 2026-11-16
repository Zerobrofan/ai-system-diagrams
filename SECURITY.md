# Security Policy

## Supported Use Cases

This repository provides educational resources, automated rendering scripts, and prompt templates for software engineering students.

## 🛡️ Best Practices for AI Diagramming

When generating architectural diagrams using Large Language Models (LLMs) such as Claude, Gemini, ChatGPT, or GitHub Copilot:

1. **Never Disclose Production Secrets**: Never paste live database passwords, internal VPC IP addresses, production API keys, or proprietary client credentials into AI prompts.
2. **Sanitize Architecture Names**: Use standardized placeholder domain names (`api.company.internal`, `10.0.1.0/24`) rather than confidential internal hostnames.
3. **Verify Third-Party Scripts**: When using automated rendering tools or downloading external packages, always review the scripts before running them in corporate or production environments.

## Reporting a Vulnerability

If you find a security flaw or an issue with the local HTTP server or scripts:
1. Please open an issue or contact **Eng. Abdallah Amir**.
2. We appreciate responsible disclosure and will address valid concerns promptly.
