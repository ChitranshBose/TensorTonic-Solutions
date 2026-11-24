import math
import numpy as np

def log_transform(values: list) -> list:
    """
    Returns the log1p-transformed values rounded to four decimals.
    """
    l = []
    for x in values:
        l.append(round(math.log(1+x),4))
    return l