import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.asarray(x, dtype = float)
    x_sorted = sorted(x)
    length = len(x)
    mean = float(np.mean(x))
    
    median = np.median(x)
    
    counts = Counter(x)
    max_count = max(counts.values())
    mode = float(min(k for k, v in counts.items() if v == max_count))
    
    
    return (mean, median, mode)