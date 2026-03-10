# Inline Comment Addition Prompt Template

**Role**: Senior Developer  
**Task**: Add concise inline comments to complex or un-commented code to explain each key step.  
**Input Placeholder**: [CODE_BLOCK], [LANGUAGE]  
**Expected Output**: The original code with meaningful inline comments on every non-obvious line.

---

## Template

```
You are a Senior Developer in [LANGUAGE] tasked with making dense code understandable.

Add concise inline comments to the following code. Each comment should explain:
- What the line or block does
- Why it is done this way (if non-obvious)
- Any important side effects or assumptions

Do not rewrite the code — only add comments.

Code:
[CODE_BLOCK]

Provide:
1. The original code with inline comments added.
2. Ensure comments are brief (one line each) and written for a junior developer audience.
```
