def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = 0
    count = 0
    
    for num in numbers:
        total += num
        count += 1
    
    average = total / count  # Runtime error possible here
    return average

def filter_outliers(data, threshold):
    """Remove values above threshold and return average."""
    filtered = [x for x in data if x < threshold]
    result = calculate_average(filtered)  # What if filtered is empty?
    return result

# Test
scores = [85, 90, 92, 88]
print(filter_outliers(scores, 80))  # Expected: ~88.75
print(filter_outliers(scores, 50))  # Expected: Error or 0?