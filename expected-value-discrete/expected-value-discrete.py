import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x, dtype = float)
    p = np.array(p, dtype = float)
    
    prod = x * p
    sum = 0
    result = 0
    for i in range(prod.shape[0]):
        sum += p[i]
        result += prod[i] 
    if sum != 1:    
        raise ValueError("Invalid probabilities")
    return result
    pass
