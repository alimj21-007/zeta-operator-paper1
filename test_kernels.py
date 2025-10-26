import pytest
import numpy as np
import kernels

def test_zeta_kernel_scalar():
    val = kernels.zeta_kernel(0.5, 0.5, 0.5)
    assert isinstance(val, (int, float, complex))

def test_gaussian_kernel_symmetry():
    x, y, sigma = 0.3, 0.7, 1.0
    assert np.isclose(
        kernels.gaussian_kernel(x, y, sigma),
        kernels.gaussian_kernel(y, x, sigma)
    )
