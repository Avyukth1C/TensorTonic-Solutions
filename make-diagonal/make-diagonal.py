import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    v = np.asarray(v, dtype = float)
    v_shape = len(v)
    D = np.diag(v.astype(float))

    return D
