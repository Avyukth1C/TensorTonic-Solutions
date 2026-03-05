def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    f = (a * x0**2) + (b * x0) + c
    def f_hat(x0):
        return (2 * a * x0) + b
    for step in range(steps):
        x0 = x0 - (lr * f_hat(x0))

    return x0
    pass