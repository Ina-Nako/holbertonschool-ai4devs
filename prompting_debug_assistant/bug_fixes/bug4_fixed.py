"""Bug 4 Fixed - Data type misuse

Intended behavior: sum values in a dict where values are numeric strings.
Fix: initialized total as 0 (int) and convert each value with int() before adding.
"""

from typing import Dict


def sum_string_values(values: Dict[str, str]) -> int:
    total = 0  # FIX: initialize as integer, not empty string

    for key, value in values.items():
        total += int(value)  # FIX: convert string to int before adding

    return total


if __name__ == "__main__":
    assert sum_string_values({"apples": "10", "oranges": "5", "pears": "2"}) == 17
    assert sum_string_values({"a": "0", "b": "0"}) == 0
    assert sum_string_values({}) == 0
    print("All tests passed.")
