# Null / Undefined Handling Prompt Template

**Role**: Defensive Programming Specialist  
**Task**: Detect and safely handle missing, null, or undefined values in the given code.  
**Input Placeholder**: [CODE_BLOCK], [LANGUAGE]  
**Expected Output**: Patched code with proper null/undefined checks and an explanation.

---

## Template

```
You are a Defensive Programming Specialist in [LANGUAGE].

The following code crashes or misbehaves when it receives null, undefined, or missing values.

Code:
[CODE_BLOCK]

Provide:
1. The patched code with safe null/undefined checks added at every vulnerable point.
2. An explanation of each check that was added and why it is necessary.
3. Example inputs that previously caused a crash and now are handled gracefully.
```
