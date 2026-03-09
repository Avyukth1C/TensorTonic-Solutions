import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x, dtype = float)
    p = np.array(p, dtype = float)
    if not np.allclose(np.sum(p), 1,rtol = 1e-6):
        raise ValueError("Invalid probabilities")

    

    return np.sum(x * p)
    pass
