import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    x = np.asarray(x, dtype = float)
    avg = np.mean(x)
    var = np.sum((x - avg) ** 2) / (len(x) - 1)
    std = np.sqrt(var)
    return (var, std)