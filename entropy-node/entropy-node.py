import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y = np.array(y)
    _, counts = np.unique(y, return_counts=True)
    probs = counts[counts > 0] / len(y)
    entropy = -np.sum(probs * np.log2(probs))
    return float(entropy)