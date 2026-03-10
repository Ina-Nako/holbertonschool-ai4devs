# Input Validation Prompt Template

**Role**: Security-Focused Developer  
**Task**: Harden the given function or endpoint by adding proper input sanitization and validation.  
**Input Placeholder**: [CODE_BLOCK], [LANGUAGE], [INPUT_SOURCES]  
**Expected Output**: Hardened version of the code with validation logic added and explained.

---

## Template

```
You are a Security-Focused Developer in [LANGUAGE].

The following function or endpoint accepts user-supplied data from [INPUT_SOURCES]
(e.g., HTTP request body, query parameters, CLI arguments) without sufficient validation.

Code:
[CODE_BLOCK]

Add proper input validation and sanitization to:
- Reject or sanitize unexpected data types, lengths, and formats
- Prevent injection attacks (SQL, command, XSS)
- Return meaningful error responses for invalid input

Provide:
1. The hardened version of the code with validation logic added.
2. Inline comments explaining each validation rule.
3. A list of the specific attack vectors that each validation rule mitigates.
```
