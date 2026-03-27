## Task 1 - User Signup Endpoint
**Estimated Time**: 20-30 minutes  
**Requirements**: Implement a `POST /users` endpoint in Node.js and Express that validates input and creates a user record in memory (array or map). Validate that `name` is non-empty and `email` is a valid email format. Prevent duplicate emails.  
**Inputs**: JSON body `{ "name": string, "email": string }`  
**Outputs**: JSON response with created user `{ "id": number, "name": string, "email": string }`  
**Acceptance Criteria**:
- Returns `201` with created user on valid input.
- Returns `400` if `name` is empty or email format is invalid.
- Returns `409` if email already exists.
- Returns `application/json` content type for all responses.

## Task 2 - Python Log Parser Utility
**Estimated Time**: 15-25 minutes  
**Requirements**: Write a Python function `summarize_log_levels(log_text: str) -> dict` that counts occurrences of `INFO`, `WARN`, and `ERROR` from multiline log text. Ignore case and ignore lines without those levels.  
**Inputs**: Multiline string, example:  
`"[10:00] INFO Start\n[10:01] error Failed\n[10:02] WARN Retry"`  
**Outputs**: Dictionary with counts, example: `{ "INFO": 1, "WARN": 1, "ERROR": 1 }`  
**Acceptance Criteria**:
- Correctly counts all three levels regardless of capitalization.
- Returns `0` for levels not present.
- Does not crash on empty input; returns all zeros.
- Includes at least 3 unit tests covering normal input, mixed case, and empty input.

## Task 3 - Frontend Form Validation
**Estimated Time**: 20-30 minutes  
**Requirements**: Build a simple HTML/CSS/JavaScript form with fields `username`, `password`, and `confirmPassword`. Validate client-side rules: username minimum 3 chars, password minimum 8 chars with at least one number, and matching passwords. Display inline error messages.  
**Inputs**: User-typed form values in browser UI  
**Outputs**: Validation state and messages in the page; success message when all validations pass  
**Acceptance Criteria**:
- Submit button does not allow successful submission when validations fail.
- Each invalid field shows a specific, readable error message.
- Clearing/fixing a field removes its error without page reload.
- On valid submission, displays success text and no error messages remain.