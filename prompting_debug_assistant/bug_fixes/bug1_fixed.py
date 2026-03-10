"""Bug 1 Fixed - Off-by-one slicing

Intended behavior: return the last n items of a list.
Fix: corrected start index from len(items) - n - 1 to len(items) - n.
"""

from typing import List, TypeVar

T = TypeVar("T")


def last_n(items: List[T], n: int) -> List[T]:
    if n <= 0:
        return []

    start = len(items) - n  # FIX: removed erroneous - 1
    return items[start:]


if __name__ == "__main__":
    assert last_n([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert last_n([1, 2, 3, 4, 5], 2) == [4, 5]
    assert last_n([1, 2, 3], 3) == [1, 2, 3]
    assert last_n([1, 2, 3], 0) == []
    print("All tests passed.")
