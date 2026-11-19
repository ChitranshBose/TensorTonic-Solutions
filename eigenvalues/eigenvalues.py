import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    x = np.linalg.eig(np.array(matrix))[0]
    x = np.sort(x)
    return x