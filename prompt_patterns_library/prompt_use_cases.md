# Prompt Use Cases

## Code Quality
- **Refactoring**
  - **Goal**: Improve readability and performance
  - **Input**: Source function in [LANGUAGE]
  - **Output**: Optimized code + explanation

- **Style Enforcement**
  - **Goal**: Enforce consistent naming and formatting
  - **Input**: Code block
  - **Output**: Rewritten code with consistent style

- **Code Review**
  - **Goal**: Identify potential issues, anti-patterns, and improvements
  - **Input**: Code snippet or file in [LANGUAGE]
  - **Output**: List of issues with suggested fixes

## Debugging
- **Error Diagnosis**
  - **Goal**: Identify the root cause of a runtime or compilation error
  - **Input**: Error message + relevant code snippet
  - **Output**: Explanation of the bug and corrected code

- **Logic Bug Detection**
  - **Goal**: Find off-by-one errors, incorrect conditions, or flawed algorithms
  - **Input**: Function with unexpected output and test case
  - **Output**: Annotated code highlighting the faulty logic and a fix

- **Null / Undefined Handling**
  - **Goal**: Detect and handle missing or undefined values safely
  - **Input**: Code block that crashes on null input
  - **Output**: Patched code with proper null checks and explanation

## Documentation
- **Docstring Generation**
  - **Goal**: Auto-generate function/class documentation
  - **Input**: Function or class definition in [LANGUAGE]
  - **Output**: Docstring in the project's doc format (JSDoc, Sphinx, etc.)

- **README Creation**
  - **Goal**: Produce a clear project overview for new contributors
  - **Input**: Project name, tech stack, and key features list
  - **Output**: Structured README with setup, usage, and contribution sections

- **Inline Comment Addition**
  - **Goal**: Explain non-obvious logic inside complex code blocks
  - **Input**: Dense or un-commented code
  - **Output**: Code with concise inline comments on each key step

## Testing
- **Unit Test Generation**
  - **Goal**: Create comprehensive unit tests covering happy paths and edge cases
  - **Input**: Function signature and description in [LANGUAGE]
  - **Output**: Test file with multiple test cases using [FRAMEWORK]

- **Edge Case Identification**
  - **Goal**: Discover boundary conditions and corner cases missed by existing tests
  - **Input**: Function or module under test
  - **Output**: List of edge cases + corresponding test stubs

- **Test Data Generation**
  - **Goal**: Produce realistic mock data for testing purposes
  - **Input**: Data schema or type definition
  - **Output**: Sample dataset in [FORMAT] (JSON, CSV, SQL, etc.)

## Security
- **Vulnerability Scanning**
  - **Goal**: Detect common security flaws (injection, XSS, insecure deserialization)
  - **Input**: Code block handling user input or external data
  - **Output**: Flagged vulnerabilities with OWASP references and remediation steps

- **Input Validation**
  - **Goal**: Ensure all external inputs are properly sanitized and validated
  - **Input**: Function or endpoint that accepts user-supplied data
  - **Output**: Hardened version of the code with validation logic added

- **Secrets Detection**
  - **Goal**: Identify hardcoded credentials, API keys, or sensitive strings
  - **Input**: Source file or code snippet
  - **Output**: List of detected secrets and recommendations for safe storage
