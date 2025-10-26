import eigen

def test_compute_eigenpairs_count():
    vals, vecs = eigen.compute_eigenpairs(grid_size=5, s=0.5, domain=(0,1), num_eigs=3)
    assert len(vals) == 3
    assert vecs.shape[1] == 3

def test_eigenvectors_normalized():
    vals, vecs = eigen.compute_eigenpairs(grid_size=5, s=0.5, domain=(0,1), num_eigs=2)
    norms = (vecs**2).sum(axis=0)**0.5
    for n in norms:
        assert abs(n - 1) < 1e-6
