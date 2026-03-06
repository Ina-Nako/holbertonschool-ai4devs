def get_first_n_elements(my_list, n):
    # This loop will return n-1 elements if n is valid, or an empty list if n=0
    result = []
    for i in range(n - 1): # Should be range(n)
        if i < len(my_list):
            result.append(my_list[i])
    return result

print(get_first_n_elements([10, 20, 30, 40, 50], 3)) # Expected: [10, 20, 30], Actual: [10, 20]
print(get_first_n_elements([1, 2], 0)) # Expected: [], Actual: []