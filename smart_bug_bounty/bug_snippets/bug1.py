def get_top_scores(scores, n):
    """
    Intended to return the top n highest scores from a list.
    """
    scores.sort() # Sorts in ascending order
    # Current issue: Slicing from the front instead of the back
    return scores[:n]

# Test case
my_scores = [10, 50, 20, 80, 90]
print(get_top_scores(my_scores, 3))
