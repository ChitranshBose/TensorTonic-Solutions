def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    top_k = set(recommended[:k])
    prec = len(top_k.intersection(set(relevant)))/k
    rec = len(top_k.intersection(set(relevant)))/len(relevant)
    return [float(prec), float(rec)]