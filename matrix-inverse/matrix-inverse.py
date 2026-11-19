import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    # Write code here
    a = np.array(A)
    if np.linalg.det(a)!=0:
        return np.linalg.inv(a)
    else:
        return None