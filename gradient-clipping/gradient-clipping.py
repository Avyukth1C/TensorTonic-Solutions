import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    g = np.asarray(g, dtype = float)
    g2 = g**2
    g_norm = np.sqrt(np.sum(g2))
    
    if g_norm <= max_norm:
        return g
    elif max_norm > 0:
        return g * (max_norm / g_norm)
    else:
        return g 
    pass