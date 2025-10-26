import numpy as np
import matplotlib.pyplot as plt

def kernel(x, y, s=1.5):
    return (x + y) ** (-s)

def trapezoid_weights(a, b, n):
    h = (b - a) / (n - 1)
    w = np.ones(n) * h
    w[0] = w[-1] = h / 2
    return w

def compute_metrics(a=0.01, b=10.0, s=1.5, grid_sizes=None):
    if grid_sizes is None:
        grid_sizes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    traces, hs_norms = [], []
    for n in grid_sizes:
        x = np.linspace(a, b, n)
        w = trapezoid_weights(a, b, n)

        # Kernel matrix
        K = kernel(x[:, None], x[None, :], s)

        # Trace ≈ sum of K(x_i, x_i) * w_i
        tr = np.sum(np.diag(K) * w)

        # HS norm^2 ≈ sum_{i,j} K(x_i, x_j)^2 * (w_i * w_j)
        hs2 = np.sum((K**2) * (w[:, None] * w[None, :]))
        hs = np.sqrt(hs2)

        traces.append(tr)
        hs_norms.append(hs)
    return grid_sizes, traces, hs_norms

def plot_convergence_png(filename="convergence_plot.png"):
    gs, traces, hs_norms = compute_metrics()
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(gs, traces, marker='o', linewidth=2, label='Trace')
    plt.plot(gs, hs_norms, marker='s', linewidth=2, label='HS norm')
    plt.xlabel('Grid size')
    plt.ylabel('Value')
    plt.title('Convergence of Trace and HS Norm')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    plot_convergence_png("convergence_plot.png")
