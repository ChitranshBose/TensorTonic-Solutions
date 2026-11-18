import math
import numpy as np
def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> list:
    """
    Returns a list of loss values.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    p_dash = np.clip(y_pred,eps,1-eps)
    l = -(y_true*np.log(p_dash)+(1-y_true)*np.log(1-p_dash))
    return l.tolist()
