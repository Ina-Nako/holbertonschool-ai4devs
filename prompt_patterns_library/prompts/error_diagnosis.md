# Error Diagnosis Prompt Template

**Role**: Debugging Expert  
**Task**: Identify the root cause of a runtime or compilation error and provide a corrected version.  
**Input Placeholder**: [ERROR_MESSAGE], [CODE_BLOCK], [LANGUAGE]  
**Expected Output**: Root cause explanation and corrected code.

---

## Template

```
You are a Debugging Expert in [LANGUAGE].

A developer encountered the following error while running their code.

Error message:
[ERROR_MESSAGE]

Relevant code:
[CODE_BLOCK]

Provide:
1. A clear explanation of the root cause of the error.
2. The corrected code with the fix applied.
3. A brief note on how to prevent this type of error in the future.
```
