from numerics.compute_hs_norm import compute_hilbert_schmidt_norm

def test_hs_norm_threshold():
    hs = compute_hilbert_schmidt_norm(grid_size=300)
    assert hs < 10.0, f"HS norm too large: {hs}"

if __name__ == "__main__":
    test_hs_norm_threshold()
    print("✅ Compactness test passed.")
