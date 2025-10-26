import os
import subprocess
import sys

def test_run_pipeline(tmp_path):
    # Run main.py with a small config
    config = tmp_path / "config.json"
    config.write_text('{"grid_size": 5, "domain": [0,1], "s": 0.5, "num_eigs": 2}')
    result = subprocess.run([sys.executable, "code/main.py"], cwd=".", capture_output=True)
    assert result.returncode == 0
