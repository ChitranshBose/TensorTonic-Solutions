import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    corr_prob = y_pred[np.arange(len(y_true)),y_true]
    
    corr_prob = np.clip(corr_prob,1e-15,1.0)
    return -np.mean(np.log(corr_prob))
    pass