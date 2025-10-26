"""
eigen.py
--------
Compute eigenvalues and eigenvectors of the zeta-inspired operator.
"""

import numpy as np
from operators import compute_weights, build_operator

def compute_eigenpairs(grid_size: int, s: float, domain: tuple, num_eigs: int = 5):
    """
    Compute the top eigenvalues and eigenvectors of the zeta-inspired operator.

    Parameters
    ----------
    grid_size : int
        Number of grid points for discretization.
    s : float
        Exponent parameter for the zeta-inspired kernel.
    domain : tuple
        Interval [a, b] for the operator (start, end).
    num_eigs : int, optional
        Number of top eigenpairs to return (default 5).

    Returns
    -------
    eigs : np.ndarray
        Array of the top eigenvalues (sorted in descending order).
    vecs : np.ndarray
        Matrix of corresponding eigenvectors (each column is an eigenvector).
    """
    a, b = domain
    # Grid points
    x = np.linspace(a, b, grid_size)
    # Trapezoid weights
    w = compute_weights(a, b, grid_size)
    # Build operator matrix
    A = build_operator(x, w, s)

    # Compute eigenvalues and eigenvectors
    eigs, vecs = np.linalg.eigh(A)

    # Sort in descending order
    idx = np.argsort(eigs)[::-1]
    eigs, vecs = eigs[idx], vecs[:, idx]

    return eigs[:num_eigs], vecs[:, :num_eigs]
