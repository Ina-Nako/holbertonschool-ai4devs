# Secrets Detection Prompt Template

**Role**: Security Auditor  
**Task**: Identify hardcoded credentials, API keys, tokens, or sensitive strings in source code.  
**Input Placeholder**: [CODE_BLOCK], [LANGUAGE]  
**Expected Output**: List of detected secrets with line references and recommendations for safe storage.

---

## Template

```
You are a Security Auditor reviewing [LANGUAGE] source code for hardcoded sensitive data.

Scan the following code for any hardcoded:
- Passwords or passphrases
- API keys or access tokens
- Private keys or certificates
- Database connection strings with credentials
- Secret keys used for signing or encryption
- Any other string that appears to be a credential or secret

Code to scan:
[CODE_BLOCK]

Provide:
1. A list of detected secrets, each with:
   - Line number(s) where the secret appears
   - Type of secret (e.g., API key, password)
   - Risk level: [Critical | High | Medium]
2. Recommendations for each finding:
   - How to remove the hardcoded value
   - Preferred safe storage mechanism (e.g., environment variables, secrets manager, vault)
3. A code snippet showing the corrected implementation using a secure alternative.
```
