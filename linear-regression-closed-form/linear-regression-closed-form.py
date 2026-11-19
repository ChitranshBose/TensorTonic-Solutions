import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    # Write code here
    x = np.array(X)
    y = np.array(y)
    a = np.linalg.inv(np.dot(np.transpose(x),x))
    b = np.dot(np.transpose(x),y)
    w = np.dot(a,b)
    return w.tolist()