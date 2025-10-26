"""
operators.py
------------
Defines functions for building the weighted operator matrix
associated with the zeta-inspired kernel.
"""

import numpy as np
from kernels import kernel_zeta

def compute_weights(a: float, b: float, n: int) -> np.ndarray:
    """
    Compute trapezoid rule weights for numerical integration.

    Parameters
    ----------
    a : float
        Start of the interval.
    b : float
        End of the interval.
    n : int
        Number of grid points.

    Returns
    -------
    np.ndarray
        Array of length n containing trapezoid rule weights.
    """
    h = (b - a) / (n - 1)
    w = np.ones(n) * h
    w[0] = w[-1] = h / 2
    return w

def build_operator(x: np.ndarray, w: np.ndarray, s: float = 1.5) -> np.ndarray:
    """
    Build the weighted kernel matrix for the integral operator.

    Parameters
    ----------
    x : np.ndarray
        1D array of grid points.
    w : np.ndarray
        1D array of trapezoid rule weights.
    s : float, optional
        Exponent parameter for the zeta-inspired kernel (default 1.5).

    Returns
    -------
    np.ndarray
        Weighted kernel matrix A approximating the integral operator.
    """
    # Kernel matrix
    K = kernel_zeta(x, x, s)

    # Apply weights symmetrically: A = W^(1/2) K W^(1/2)
    W_sqrt = np.sqrt(w)
    A = K * (W_sqrt[:, None] * W_sqrt[None, :])
    return A
