# Risk Assessment

Codebase: osCommerce 2.x (legacy PHP e-commerce platform)
Source: https://github.com/osCommerce/oscommerce2

| Risk | Severity | Notes |
|---|---|---|
| SQL injection in database queries | High | Multiple query paths build SQL via string concatenation with request data instead of prepared statements |
| Cross-site scripting in rendered output | High | Dynamic values are printed into HTML without consistent output escaping, enabling stored or reflected script execution |
| Session fixation after authentication | High | Session identifiers are not reliably rotated after login, increasing account takeover risk |
| CSRF exposure on state-changing actions | High | Legacy form handling does not consistently enforce anti-CSRF tokens for checkout and account actions |
| Use of removed/deprecated PHP APIs | High | Core flows depend on old mysql and session-era functions incompatible with modern PHP runtimes |
| Inconsistent checkout data integrity | Medium | Large procedural checkout flow lacks transaction boundaries, so partial failures can leave orders and inventory out of sync |
| No automated regression test suite | Medium | Critical payment, cart, and order paths are untested, raising defect risk during fixes and upgrades |
| Limited observability and incident diagnostics | Medium | Errors are weakly logged and monitoring is minimal, delaying root-cause analysis during production failures |
