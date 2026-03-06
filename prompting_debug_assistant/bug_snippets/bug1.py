"""Bug 1 - Off-by-one slicing

Intended behavior: return the last n items of a list.
Issue: returns n+1 items when n < len(items).
"""

from typing import List, TypeVar

T = TypeVar("T")


def last_n(items: List[T], n: int) -> List[T]:
    if n <= 0:
        return []

    start = len(items) - n - 1  # BUG: off-by-one; should be len(items) - n
    return items[start:]


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print(last_n(data, 2))  # expected [4, 5] but returns [3, 4, 5]
