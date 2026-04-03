# Risk Assessment

Codebase: osCommerce 2.x (legacy PHP e-commerce platform)
Source: https://github.com/osCommerce/oscommerce2

| Risk | Severity | Notes |
|---|---|---|
| SQL injection vulnerabilities | High | Raw `$_GET`/`$_POST` values interpolated directly into SQL strings throughout the codebase; no prepared statements used |
| Deprecated and removed PHP functions | High | Heavy reliance on `mysql_query()`, `mysql_real_escape_string()`, and `session_register()`, all removed in PHP 7+ |
| Cross-site scripting (XSS) | High | User-supplied data echoed into HTML without `htmlspecialchars()` escaping, enabling stored and reflected XSS attacks |
| Session fixation and weak authentication | High | Session ID is never regenerated after login; no secure cookie flags enforced, allowing session hijacking attacks |
| No automated tests | Medium | Zero unit, integration, or end-to-end tests in the core codebase; regressions are only discovered in production |
| Tight coupling and god scripts | Medium | Business logic, SQL queries, and HTML rendering coexist in single files exceeding 500 lines, making changes risky and refactoring costly |
| No logging or error handling | Medium | Errors are silently suppressed or echoed directly to users; no centralized logging makes diagnosing production failures very difficult |
| Hardcoded database configuration | Medium | Database credentials and connection settings are stored in plain-text PHP config files with no environment variable abstraction |
| Outdated third-party dependencies | Low | Bundled jQuery 1.x (EOL since 2016) and other manually copied libraries with no versioning or package manager |
| No dependency management | Low | No Composer or npm support; all libraries are manually copied files with no version pinning or vulnerability scanning |
