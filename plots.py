"""
plots.py
--------
Visualization utilities for the zeta-inspired operator.
"""

import numpy as np
import matplotlib.pyplot as plt
from kernels import kernel_zeta

def plot_heatmap(grid_size: int, s: float, domain: tuple, filename: str = "heatmap_kernel.png"):
    """
    Generate and save a heatmap of the kernel matrix (x+y)^(-s).

    Parameters
    ----------
    grid_size : int
        Number of grid points for discretization.
    s : float
        Exponent parameter for the zeta-inspired kernel.
    domain : tuple
        Interval [a, b] for the operator (start, end).
    filename : str, optional
        Path to save the heatmap image (default 'heatmap_kernel.png').
    """
    a, b = domain
    # Grid points
    x = np.linspace(a, b, grid_size)
    # Kernel matrix
    K = kernel_zeta(x, x, s)

    # Plot heatmap
    plt.figure(figsize=(6, 5), dpi=150)
    im = plt.imshow(K, origin="lower", cmap="viridis", extent=[a, b, a, b], aspect="auto")
    plt.colorbar(im, label="(x+y)^(-s)")
    plt.title(f"Heatmap of Kernel Matrix (s={s})")
    plt.xlabel("y")
    plt.ylabel("x")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
