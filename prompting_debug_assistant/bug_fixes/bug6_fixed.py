"""Bug 6 Fixed - Loop logic issue (infinite loop)

Intended behavior: find the first pair of consecutive numbers that sum to target.
Fix: moved i += 1 outside the if block so the index always advances.
"""

from typing import List, Optional, Tuple


def first_consecutive_pair(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    i = 0
    while i < len(nums) - 1:
        if nums[i] + nums[i + 1] == target:
            return (nums[i], nums[i + 1])
        i += 1  # FIX: always increment, not only on match

    return None


if __name__ == "__main__":
    assert first_consecutive_pair([1, 2, 4, 3], 7) == (4, 3)
    assert first_consecutive_pair([1, 2, 4, 8], 7) is None
    assert first_consecutive_pair([3, 4], 7) == (3, 4)
    assert first_consecutive_pair([], 7) is None
    print("All tests passed.")
