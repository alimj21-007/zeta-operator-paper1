import numpy as np
import operators
import kernels

def test_build_operator_shape():
    op = operators.build_operator(kernels.gaussian_kernel, grid_size=5, domain=(0,1))
    assert op.shape == (5,5)

def test_apply_operator_vector():
    op = np.eye(3)
    vec = np.array([1,2,3])
    result = operators.apply_operator(op, vec)
    assert np.allclose(result, vec)
