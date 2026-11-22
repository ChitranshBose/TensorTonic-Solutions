from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.array(x)
    c = Counter(x)
    mode = c.most_common()[0][0]
    d = {
        "mean": float(np.mean(x)),
        "median": float(np.median(x)),
        "mode": float(mode)
    }
    return d