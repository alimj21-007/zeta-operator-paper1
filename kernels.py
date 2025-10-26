"""
kernels.py
----------
Defines kernel functions for the zeta-inspired operator and alternatives.
"""

import numpy as np

def kernel_zeta(x: np.ndarray, y: np.ndarray, s: float = 1.5) -> np.ndarray:
    """
    Zeta-inspired kernel: (x+y)^(-s).

    Parameters
    ----------
    x : np.ndarray
        1D array of grid points along x-axis.
    y : np.ndarray
        1D array of grid points along y-axis.
    s : float, optional
        Exponent parameter (default 1.5).

    Returns
    -------
    np.ndarray
        Kernel matrix K[i,j] = (x[i] + y[j])^(-s).
    """
    return (x[:, None] + y[None, :]) ** (-s)


def kernel_gaussian(x: np.ndarray, y: np.ndarray, sigma: float = 1.0) -> np.ndarray:
    """
    Gaussian kernel: exp(-((x-y)^2)/(2*sigma^2)).

    Parameters
    ----------
    x : np.ndarray
        1D array of grid points along x-axis.
    y : np.ndarray
        1D array of grid points along y-axis.
    sigma : float, optional
        Standard deviation parameter (default 1.0).

    Returns
    -------
    np.ndarray
        Kernel matrix K[i,j] = exp(-((x[i]-y[j])^2)/(2*sigma^2)).
    """
    return np.exp(-((x[:, None] - y[None, :]) ** 2) / (2 * sigma ** 2))


def kernel_exponential(x: np.ndarray, y: np.ndarray, alpha: float = 1.0) -> np.ndarray:
    """
    Exponential kernel: exp(-alpha*|x-y|).

    Parameters
    ----------
    x : np.ndarray
        1D array of grid points along x-axis.
    y : np.ndarray
        1D array of grid points along y-axis.
    alpha : float, optional
        Decay parameter (default 1.0).

    Returns
    -------
    np.ndarray
        Kernel matrix K[i,j] = exp(-alpha*|x[i]-y[j]|).
    """
    return np.exp(-alpha * np.abs(x[:, None] - y[None, :]))
