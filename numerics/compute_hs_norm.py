import numpy as np
from operators.zeta_operator import zeta_kernel, weighted_measure

def compute_hilbert_schmidt_norm(grid_size=200, s=1.5, alpha=0.5, beta=1.0, domain=(0.01, 10)):
    """Compute HS norm of the operator numerically."""
    x = np.linspace(domain[0], domain[1], grid_size)
    y = np.linspace(domain[0], domain[1], grid_size)
    dx = x[1] - x[0]
    dy = y[1] - y[0]

    X, Y = np.meshgrid(x, y)
    K = zeta_kernel(X, Y, s)
    W = weighted_measure(X, alpha, beta) * weighted_measure(Y, alpha, beta)

    hs_integrand = np.abs(K)**2 * W
    hs_norm_squared = np.sum(hs_integrand) * dx * dy
    hs_norm = np.sqrt(hs_norm_squared)
    return hs_norm

if __name__ == "__main__":
    hs = compute_hilbert_schmidt_norm()
    print(f"Hilbert–Schmidt norm ≈ {hs:.6f}")
