import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    v = np.asarray(v, dtype = float)
    w = np.asarray(w, dtype = float)
    v_norm = np.linalg.norm(v)
    w_norm = np.linalg.norm(w)
    if v_norm == 0.0 or w_norm == 0.0: 
        return np.nan
        
    cos = np.dot(v, w)/(v_norm * w_norm)
    theta = np.arccos(np.clip(cos, -1, 1))
    
    return float(theta)