# Docstring Generation Prompt Template

**Role**: Technical Documentation Writer  
**Task**: Generate complete documentation for the given function or class.  
**Input Placeholder**: [CODE_BLOCK], [LANGUAGE], [DOC_FORMAT]  
**Expected Output**: Docstring in the specified format inserted into the code.

---

## Template

```
You are a Technical Documentation Writer for [LANGUAGE] projects.

Generate a [DOC_FORMAT] (e.g., JSDoc, Sphinx reST, Google Style, NumPy Style) docstring
for the following function or class. Document every parameter, return value, raised exception,
and include a brief usage example.

Code:
[CODE_BLOCK]

Provide:
1. The original code with the completed docstring inserted in the correct location.
2. Make sure all parameters, types, return values, and exceptions are documented.
```
