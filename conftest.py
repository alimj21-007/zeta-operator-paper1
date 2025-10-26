import pytest
import json
import numpy as np

@pytest.fixture
def small_config(tmp_path):
    """Fixture: create a small config.json for quick tests."""
    cfg = {
        "grid_size": 5,
        "domain": [0.0, 1.0],
        "s": 0.5,
        "num_eigs": 2
    }
    cfg_file = tmp_path / "config.json"
    cfg_file.write_text(json.dumps(cfg))
    return cfg_file

@pytest.fixture
def output_dir(tmp_path):
    """Fixture: temporary directory for outputs (csv, png, logs)."""
    return tmp_path

@pytest.fixture
def sample_kernel():
    """Fixture: a simple symmetric kernel for testing operators."""
    def kernel(x, y, s=1.0):
        return np.exp(-abs(x-y))  # simple exponential kernel
    return kernel
