import numpy as np

def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    W = np.array(W, dtype = float)
    fan_in = np.array(fan_in, dtype = float)
    
    L = np.sqrt(6 / fan_in)
    W_new = W * 2 * L - L

    return W_new