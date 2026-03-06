def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    if len(numbers) > 0:
        return total / len(numbers)
    else:
        return 0

# This line is intentionally missing a closing parenthesis to cause a SyntaxError
print("The average is:", calculate_average([10, 20, 30])
