def get_top_scores(scores, n):
    """
    FIXED: Returns the top n highest scores from a list.
    """
    scores.sort() 
    # Fix: Slice from the end of the list to get the highest numbers
    return scores[-n:]

my_scores = [10, 50, 20, 80, 90]
print(get_top_scores(my_scores, 3)) # Output: [50, 80, 90]
