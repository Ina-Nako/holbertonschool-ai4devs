def find_max(numbers):
    """Return the maximum value in a list of numbers."""
    max_val = 0
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


# Test cases
print(find_max([3, 7, 2, 8, 1]))        # Expected: 8
print(find_max([-5, -1, -10, -3]))       # Expected: -1
print(find_max([0, 0, 0]))              # Expected: 0
