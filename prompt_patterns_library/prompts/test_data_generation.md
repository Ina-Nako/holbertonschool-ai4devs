# Test Data Generation Prompt Template

**Role**: Data Engineer  
**Task**: Generate realistic mock data matching the given schema or type definition.  
**Input Placeholder**: [SCHEMA], [FORMAT], [NUM_RECORDS]  
**Expected Output**: A sample dataset in the specified format ready to use in tests.

---

## Template

```
You are a Data Engineer generating test data for software testing purposes.

Generate [NUM_RECORDS] realistic mock records that conform to the following schema or type definition.

Schema / Type definition:
[SCHEMA]

Output format: [FORMAT] (e.g., JSON, CSV, SQL INSERT statements, Python list of dicts)

Requirements:
- Include a variety of realistic values (avoid all-null or trivially repeated data).
- Include at least one record with boundary values (empty string, zero, max length, etc.).
- Include at least one record that represents an invalid/edge case input if applicable.

Provide:
1. The generated dataset in [FORMAT].
2. A brief note on any special records included and why.
```
