import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    
    x = np.asarray(x, dtype = float) 
    return x * (1 / (1 + np.exp(np.clip(-x, -20, 20))))
    pass