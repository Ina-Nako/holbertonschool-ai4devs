"""Bug 4 - Data type misuse

Intended behavior: sum values in a dict where values are numeric strings.
Issue: uses string concatenation instead of numeric addition.
"""

from typing import Dict


def sum_string_values(values: Dict[str, str]) -> int:
    total = ""  # BUG: should start at 0

    for key, value in values.items():
        total += value  # BUG: concatenates strings

    return total  # BUG: returns a string, not an int


if __name__ == "__main__":
    d = {"apples": "10", "oranges": "5", "pears": "2"}
    print(sum_string_values(d))  # expected 17 but returns "1052"
