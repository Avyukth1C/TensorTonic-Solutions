import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)
    A_shape = A.shape
    N, M = A_shape
    i, j = 0, 0 
    AT = np.zeros((M, N))
    
    for i in range(0, N):
        for j in range(0, M):
            AT[j, i] = A[i, j]
    
    return AT
    
    pass
