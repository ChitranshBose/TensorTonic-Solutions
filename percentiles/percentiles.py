import numpy as np
import math as m
def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    # Write code here
    x = np.sort(np.array(x))
    n = len(x)
    lst = []
    for i in q:
        r = (i/100)*(n-1)
        l = m.floor(r)
        u = m.ceil(r)
        w = r-l
        res = (1-w)*x[l]+w*x[u]
        lst.append(res)
    res = np.array(lst)
    return res