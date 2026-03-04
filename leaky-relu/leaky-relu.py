import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    x = np.asarray(x, dtype = float)
    result = np.where(x < 0, alpha * x, x)
    
    return result
    pass