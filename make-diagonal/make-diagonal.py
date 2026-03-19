import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    v = np.asarray(v, dtype = float)
    v_shape = len(v)
    D = np.zeros((v_shape, v_shape))
    for i in range(D.shape[0]):
        for j in range(D.shape[1]):
            if i == j:
                D[i,j] = v[i]

    return D
