"""
convergence.py
--------------
Compute and visualize convergence metrics (Trace and Hilbert–Schmidt norm)
for the zeta-inspired operator.
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
from operators import compute_weights, build_operator

def compute_metrics(a: float = 0.01, b: float = 10.0, s: float = 1.5, grid_sizes=None):
    """
    Compute Trace and HS norm for different grid sizes.

    Parameters
    ----------
    a : float
        Start of the domain (default 0.01).
    b : float
        End of the domain (default 10.0).
    s : float
        Exponent parameter for the kernel (default 1.5).
    grid_sizes : list[int], optional
        List of grid sizes to test. Default: [50,100,...,500].

    Returns
    -------
    grid_sizes : list[int]
        Grid sizes used.
    traces : list[float]
        Trace values for each grid size.
    hs_norms : list[float]
        Hilbert–Schmidt norm values for each grid size.
    """
    if grid_sizes is None:
        grid_sizes = list(range(50, 501, 50))

    traces, hs_norms = [], []
    for n in grid_sizes:
        x = np.linspace(a, b, n)
        w = compute_weights(a, b, n)
        A = build_operator(x, w, s)

        tr = np.sum(np.diag(A))
        hs = np.linalg.norm(A, 'fro')

        traces.append(tr)
        hs_norms.append(hs)

    return grid_sizes, traces, hs_norms


def plot_convergence(filename: str = "convergence_plot.png"):
    """
    Plot convergence of Trace and HS norm as grid size increases.

    Parameters
    ----------
    filename : str
        Path to save the plot (default 'convergence_plot.png').
    """
    gs, traces, hs_norms = compute_metrics()

    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(gs, traces, marker='o', label="Trace")
    plt.plot(gs, hs_norms, marker='s', label="HS norm")
    plt.xlabel("Grid size")
    plt.ylabel("Value")
    plt.title("Convergence of Trace and HS Norm")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


def save_convergence_metrics(filename: str = "convergence_metrics.csv"):
    """
    Save convergence metrics (Trace and HS norm) to a CSV file.

    Parameters
    ----------
    filename : str
        Path to save the CSV file (default 'convergence_metrics.csv').
    """
    gs, traces, hs_norms = compute_metrics()

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["grid_size", "trace", "hs_norm"])
        for g, t, h in zip(gs, traces, hs_norms):
            writer.writerow([g, f"{t:.6f}", f"{h:.6f}"])
