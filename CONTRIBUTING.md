## 🔒 Secrets & Environment Management

- **No Hardcoded Secrets**: Never hardcode API keys, passwords, or tokens directly in the source code.
- **Environment Variables**: Use `.env.example` as a template. Copy it to create your local `.env` file and populate your actual credentials for local development.
- **Git Ignore**: Ensure that `.env` and any files containing secret keys are kept out of version control and properly listed in `.gitignore`.