import numpy as np
import matplotlib.pyplot as plt
from numerics.compute_hs_norm import compute_hilbert_schmidt_norm

def plot_hs_convergence():
    grid_sizes = np.arange(50, 501, 50)
    hs_values = []

    for N in grid_sizes:
        hs = compute_hilbert_schmidt_norm(grid_size=N)
        hs_values.append(hs)
        print(f"Grid size {N}: HS norm ≈ {hs:.6f}")

    plt.figure(figsize=(8, 5))
    plt.plot(grid_sizes, hs_values, marker='o', linestyle='-', color='darkblue')
    plt.title("Convergence of Hilbert–Schmidt Norm")
    plt.xlabel("Grid Size")
    plt.ylabel("HS Norm")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../../data/results/convergence_plot.png")
    plt.show()

if __name__ == "__main__":
    plot_hs_convergence()
