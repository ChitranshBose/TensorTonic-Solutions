import numpy as np

def ridge_regression(X: list, y: list, lam: float) -> list:
    """
    Returns the ridge-regression weight vector.
    """
    # Write code here
    x = np.array(X)
    y = np.array(y)
    iden = lam*(np.eye(len(x[0]),len(x[0])))
    a = np.dot(np.transpose(x), x)+ iden
    a = np.linalg.inv(a)
    b = np.dot(np.transpose(x),y)
    w = np.dot(a,b)
    return w.tolist()