# AI Explanations of Complex Code – osCommerce 2.x

**Codebase:** osCommerce 2.x (legacy PHP e-commerce platform)
**Source:** https://github.com/osCommerce/oscommerce2

---

## Section 1 – Raw SQL Query Construction (`catalog/product_info.php`)

```php
$product_query = tep_db_query("SELECT p.products_id, pd.products_name,
  pd.products_description, p.products_price
  FROM " . TABLE_PRODUCTS . " p,
  " . TABLE_PRODUCTS_DESCRIPTION . " pd
  WHERE p.products_status = '1'
  AND p.products_id = '" . (int)$_GET['products_id'] . "'
  AND pd.language_id = '" . (int)$languages_id . "'");
```

- **Plain English**: Builds a SQL string by directly concatenating user-supplied URL parameters (e.g., `$_GET['products_id']`) into the query. It casts the value to `int` as a lightweight guard, then sends the assembled string to the database.
- **Pattern**: String interpolation for query construction — no prepared statements, no parameterized queries.
- **Issues**:
  - The `(int)` cast only protects this specific instance; the same pattern elsewhere in the codebase omits even that cast, leaving raw `$_GET`/`$_POST` values in SQL strings — a textbook SQL injection vulnerability.
  - Deprecated `mysql_*` extension is used under `tep_db_query()`, removed in PHP 7.
  - No error handling: a failed query silently returns `false`, potentially crashing the page with no useful feedback.
- **Improvements**:
  - Replace `tep_db_query()` with PDO or MySQLi prepared statements and bound parameters.
  - Centralize all DB access in a repository layer; remove inline queries from view scripts.
  - Add query error logging via a proper logging framework (e.g., Monolog).

---

## Section 2 – Checkout Process (`catalog/checkout_process.php`)

```php
if (isset($_SESSION['sendto']) && ($_SESSION['sendto'] > 0)) {
  if (isset($_SESSION['cart']) && ($_SESSION['cart']->count_contents() > 0)) {
    if (tep_session_is_registered('customer_id')) {
      // ... 400+ more lines: order calculation, stock check,
      //     payment module processing, email assembly, redirect
    } else {
      tep_redirect(tep_href_link(FILENAME_LOGIN, '', 'SSL'));
    }
  } else {
    tep_redirect(tep_href_link(FILENAME_SHOPPING_CART));
  }
} else {
  tep_redirect(tep_href_link(FILENAME_CHECKOUT_SHIPPING, '', 'SSL'));
}
```

- **Plain English**: One giant script that performs every step of completing an order — verifying the session, checking cart contents, confirming login, calculating totals, processing payment, decrementing stock, building a confirmation email, and redirecting the user. All of this is done sequentially inside deeply nested `if` blocks, with no separation into functions or classes.
- **Pattern**: "God script" — a single procedural file handling multiple distinct responsibilities; deep nesting (4–6 levels) instead of early-return / guard clauses.
- **Issues**:
  - Extremely high cognitive complexity; a change to payment logic risks breaking email or stock logic.
  - No rollback mechanism — if the email step fails after stock is decremented, inventory is corrupted.
  - Zero automated tests; any regression is discovered in production.
  - Session checks rely on `tep_session_is_registered()`, a wrapper around the removed `session_is_registered()` PHP function.
- **Improvements**:
  - Extract into service classes: `OrderService`, `PaymentService`, `InventoryService`, `NotificationService`.
  - Use database transactions to wrap order creation and stock decrement atomically.
  - Replace nested `if` chains with guard clauses and early returns.
  - Add integration tests covering the happy path and failure scenarios.

---

## Section 3 – Session and Authentication Handling (`includes/application_top.php`)

```php
if (PHP_VERSION < 4.3) {
  tep_session_start();
} else {
  if (!tep_session_start()) {
    tep_redirect(tep_href_link(FILENAME_LOGIN));
  }
}

if (!tep_session_is_registered('customer_id')) {
  tep_session_register('customer_id');
  $customer_id = '';
}
// No session_regenerate_id() call after login
```

- **Plain English**: Starts a PHP session and checks whether a `customer_id` variable is registered in it. If not, it registers the variable and sets it to an empty string. The session ID is never regenerated after a successful login.
- **Pattern**: Legacy session API (`session_register()`, removed in PHP 5.4) combined with no post-authentication ID rotation.
- **Issues**:
  - **Session fixation**: an attacker can set a known session ID before login; after the user authenticates, that same ID remains valid, granting the attacker access.
  - `session_register()` relies on `register_globals`, a PHP directive removed in PHP 5.4.
  - PHP version check targets PHP < 4.3, which has been EOL since 2007 — dead code that adds noise.
  - No HTTPS-only (`session.cookie_secure`) or `HttpOnly` (`session.cookie_httponly`) flags enforced in code.
- **Improvements**:
  - Call `session_regenerate_id(true)` immediately after successful login to rotate the session ID.
  - Remove all uses of `session_register()` and `$_SESSION`-via-globals; use `$_SESSION` directly.
  - Set `session.cookie_secure`, `session.cookie_httponly`, and `session.cookie_samesite` in configuration.
  - Implement a CSRF token tied to the session for all state-changing requests.

---

## Section 4 – Template Rendering and Output Escaping (`catalog/index.php`)

```php
echo '<td class="productListing-data">';
echo '<a href="' . tep_href_link(FILENAME_PRODUCT_INFO,
  'products_id=' . $listing['products_id']) . '">';
echo '<img src="' . DIR_WS_IMAGES . $listing['products_image'] . '"
  border="0" alt="' . $listing['products_name'] . '">';
echo '</a>';
echo '<br>' . $listing['products_name'];
echo '<br>' . $currencies->display_price($listing['products_price'],
  tep_get_tax_rate($listing['products_tax_class_id']));
echo '</td>';
```

- **Plain English**: Renders a product listing card by echoing raw HTML strings built from database values. Product names and image paths fetched from the database are inserted directly into the HTML without encoding.
- **Pattern**: Mixed PHP/HTML via string concatenation; no templating engine; no output escaping.
- **Issues**:
  - **Stored XSS**: if a product name contains `<script>alert(1)</script>` (injected via the admin panel or a compromised DB), it is rendered verbatim in every visitor's browser.
  - `border="0"` is deprecated HTML 4 presentational attribute — indicative of the overall code age.
  - Logic (pricing, tax calculation) is embedded directly in the view layer, violating separation of concerns.
  - Maintenance is very difficult: changing the layout requires hunting through hundreds of `echo` lines.
- **Improvements**:
  - Wrap all user-originated values in `htmlspecialchars($value, ENT_QUOTES, 'UTF-8')` before output.
  - Introduce a templating engine (Twig, Blade) to enforce automatic escaping and separate view from logic.
  - Move price/tax computation to a dedicated service or presenter before passing data to the template.

---

## Section 5 – Input Sanitization (`includes/functions/database.php`)

```php
function tep_db_prepare_input($string) {
  if (is_string($string)) {
    return trim(addslashes($string));
  } elseif (is_numeric($string)) {
    return $string;
  } else {
    return false;
  }
}
```

- **Plain English**: Attempts to sanitize user input before it is used in a SQL query. For strings, it trims whitespace and calls `addslashes()` to escape quotes. For numbers, it passes the value through unchanged. For anything else, it returns `false`.
- **Pattern**: Manual blacklist-style escaping using `addslashes()` — the historic PHP approach before prepared statements existed.
- **Issues**:
  - `addslashes()` is **not** a safe SQL escaping function; its behavior depends on the active character set and does not protect against all SQL injection vectors (e.g., multi-byte character exploits in older MySQL/charset combinations).
  - Returns `false` for non-string/non-numeric input (arrays, objects), which silently produces the string `""` when interpolated into SQL — not an error, just silent data corruption.
  - The function is only safe when the caller both uses it **and** quotes the value correctly in the query; neither is enforced.
  - `addslashes()` was explicitly documented by PHP as insufficient for DB escaping even in the PHP 4 era.
- **Improvements**:
  - Delete `tep_db_prepare_input()` entirely and replace all call sites with PDO prepared statements and bound parameters — escaping becomes unnecessary.
  - If a full migration is blocked, at minimum replace `addslashes()` with `mysqli_real_escape_string()` and enforce the connection charset as `utf8mb4`.
  - Add a static analysis rule (e.g., PHPStan, Psalm) to flag any direct string interpolation into SQL as an error.
