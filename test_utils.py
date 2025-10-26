import utils
import json

def test_load_config(tmp_path):
    cfg_file = tmp_path / "config.json"
    cfg_file.write_text(json.dumps({"grid_size": 5}))
    cfg = utils.load_config(cfg_file)
    assert cfg["grid_size"] == 5

def test_save_csv(tmp_path):
    outfile = tmp_path / "data.csv"
    utils.save_csv(outfile, ["a","b"], [[1,2],[3,4]])
    text = outfile.read_text()
    assert "a,b" in text
