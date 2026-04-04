import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x)
    p = np.array(p)

    if len(x) != len(p):
        raise ValueError("Lengths of x and p must be equal.")
        
    # Check if any probability is negative or greater than 1
    if np.any((p < 0) | (p > 1)):
        raise ValueError("Probabilities must be between 0 and 1.")
        
    # Check if probabilities sum to 1 (using isclose for floating-point math)
    if not np.isclose(np.sum(p), 1.0):
        raise ValueError("The sum of probabilities must equal 1.")
    
    expected_value_discrete = np.sum(x*p)

    return expected_value_discrete


x = [1, 2, 3]
p = [0.2, 0.5, 0.3]
print(expected_value_discrete(x, p))
