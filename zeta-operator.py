import numpy as np

def zeta_kernel(x, y, s=1.5):
    """Zeta-inspired kernel function: symmetric and decaying."""
    return 1 / ((x + y)**s)

def weighted_measure(x, alpha=0.5, beta=1.0):
    """Weight function for Hilbert space: x^α e^{-βx}"""
    return x**alpha * np.exp(-beta * x)
