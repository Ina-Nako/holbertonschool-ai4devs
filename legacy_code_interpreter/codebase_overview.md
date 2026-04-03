# Codebase Overview - osCommerce (Legacy E-Commerce Platform)

## Age
- **First release:** March 2000 (originally named "The Exchange Project")
- **Last major version update:** osCommerce 2.4 released in 2020, but the core architecture dates to 2.2 (2006) and has changed minimally since
- **Active development span:** ~24 years, though the codebase is widely considered architecturally stagnant since 2006
- **Repository:** https://github.com/osCommerce/oscommerce2

## Size
- ~85,000 LOC across the osCommerce 2.x branch
- Primarily **PHP** (~72,000 LOC), with inline HTML, CSS, and JavaScript
- ~1,200 files across catalog, admin, and includes directories
- No separation of concerns — business logic, HTML templates, and SQL queries coexist in the same files

## Dependencies
| Dependency | Version Required | Status |
|---|---|---|
| PHP | 4.x–5.x target (8.x partially supported) | PHP 4 reached EOL in 2008 |
| MySQL | 4.x / 5.x | MySQL 4.x EOL since 2008 |
| `mysql_*` functions | Native PHP extension | Removed in PHP 7.0 |
| mcrypt | PHP extension | Deprecated in PHP 7.1, removed in PHP 7.2 |
| register_globals | PHP ini directive | Removed in PHP 5.4 |
| jQuery | 1.x (bundled) | EOL since 2016 |
| No package manager | Manual file inclusion via `require`/`include` | No Composer or npm support |

## Architecture & Structure
- **No MVC pattern** — controller logic, view rendering, and database queries are mixed in the same scripts
- **Flat file routing** — each page is a standalone PHP script (e.g., `product_info.php`, `checkout_process.php`), no centralized router
- **Global variables used extensively** — relies on `$_GET`, `$_POST`, `$_SESSION`, and custom globals throughout
- **Template system** — rudimentary; HTML is generated via concatenated PHP strings or inline `echo` statements
- **No autoloading** — all includes are manual and scattered

## Known Issues & Pain Points
- **No automated tests** — zero unit, integration, or end-to-end tests in the core codebase
- **SQL injection vulnerabilities** — raw string interpolation in SQL queries; no use of prepared statements
  ```php
  // Example of vulnerable query pattern found throughout codebase
  $query = "SELECT * FROM products WHERE products_id = " . $_GET['products_id'];
  ```
- **XSS vulnerabilities** — user-supplied input rendered without consistent sanitization
- **Deprecated PHP functions** — heavy reliance on `mysql_query()`, `mysql_real_escape_string()`, `ereg()`, all removed in modern PHP
- **register_globals dependency** — legacy code in some modules assumes variables are auto-populated from request data
- **Tight coupling** — database queries hardcoded throughout view files; no repository or service layer
- **No dependency management** — third-party libraries are manually copied into the repository with no versioning
- **Session handling weaknesses** — session fixation and insufficient session regeneration on authentication
- **Mixed encoding** — inconsistent use of UTF-8 vs. ISO-8859-1 across files
- **No logging framework** — errors silently suppressed or echoed directly to the user
- **High cognitive complexity** — some core files (e.g., `catalog/checkout_process.php`) exceed 500 lines with no abstraction
- **Difficult extensibility** — the "contribution" (plugin) system requires directly patching core files, making upgrades destructive

## Summary
osCommerce 2.x is a representative example of early-2000s PHP development practices. Its legacy issues stem from being written before modern PHP conventions (PSR standards, Composer, OOP patterns) were established. It remains in production use on thousands of sites, making it a high-risk legacy system with documented security advisories and no clear migration path without a full rewrite.
