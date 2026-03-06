"""Bug 6 - Loop logic issue (infinite loop)

Intended behavior: find the first pair of consecutive numbers that sum to target.
Issue: index increments only on match.
"""

from typing import List, Optional, Tuple


def first_consecutive_pair(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    i = 0
    while i < len(nums) - 1:
        if nums[i] + nums[i + 1] == target:
            i += 1  # BUG: increment happens only on match
            return (nums[i - 1], nums[i])

        # BUG: missing i += 1 here -> infinite loop if no pair matches

    return None


if __name__ == "__main__":
    # WARNING: Running the next line would loop forever because no pair sums to 7.
    # print(first_consecutive_pair([1, 2, 4, 8], 7))
    # Use a case where the match happens immediately, so this demo does not hang.
    print(first_consecutive_pair([4, 3, 1], 7))  # expected (4, 3)
