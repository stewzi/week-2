import numpy as np


def ways(n):
    """Return the number of ways to make n cents with pennies and nickels."""
    if n < 0:
        return 0
    return n // 5 + 1


def lowest_score(names, scores):
    """Return the name associated with the lowest score."""
    names = np.asarray(names)
    scores = np.asarray(scores)
    return names[np.argmin(scores)]


def sort_names(names, scores):
    """Return names ordered from highest to lowest score."""
    names = np.asarray(names)
    scores = np.asarray(scores)
    descending_score_indices = np.argsort(-scores, kind="stable")
    return names[descending_score_indices]
