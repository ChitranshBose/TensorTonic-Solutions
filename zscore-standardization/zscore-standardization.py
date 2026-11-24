import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    x = np.array(X)
    m = np.mean(x,axis=axis,keepdims=True)
    s = np.std(x,axis=axis, keepdims=True)
    s = np.where(s>eps,s,1.0 )
    res = (x-m)/s
    return res