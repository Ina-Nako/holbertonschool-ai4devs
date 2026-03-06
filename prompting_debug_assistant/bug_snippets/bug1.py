def get_last_n_items(items, n):
    """Return the last n items from a list."""
    if n <= 0 or n > len(items):
        return []
    
    start_index = len(items) - n
    return items[start_index:]

def main():
    my_list = [1, 2, 3, 4, 5]
    print(get_last_n_items(my_list, 3))  # Expected: [3, 4, 5]
    print(get_last_n_items(my_list, 5))  # Expected: [1, 2, 3, 4, 5]
    print(get_last_n_items(my_list, 0))  # Expected: []

if __name__ == "__main__":
    main()