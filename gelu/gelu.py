import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype = float)
    """
    
    x = np.array(x, dtype = float)

    x_erf = np.vectorize(math.erf, otypes = [float])

    erf_term = x_erf(x / math.sqrt(2))
    return (0.5*(x))*(1 + erf_term)
    pass