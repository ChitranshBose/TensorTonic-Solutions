import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # Write code here
    mat = np.zeros((len(v),len(v)))
    mat[np.arange(len(v)),np.arange(len(v))] = v 
    return mat