import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.array(x)
    xd = np.mean(x)
    n = len(x)
    sq = np.sum((x-xd)**2)/(n-1)
    s = np.sqrt(sq)
    return {"variance":float(sq), "standard_deviation":float(s)}
    pass