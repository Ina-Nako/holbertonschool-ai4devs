def last_n_items(items, n):
    """Return the last n items of a list."""
    if n <= 0:
        return []
    return items[len(items) - n + 1:]


# Test cases
print(last_n_items([1, 2, 3, 4, 5], 2))   # Expected: [4, 5]
print(last_n_items([1, 2, 3, 4, 5], 5))   # Expected: [1, 2, 3, 4, 5]
print(last_n_items([10, 20, 30], 1))       # Expected: [30]
