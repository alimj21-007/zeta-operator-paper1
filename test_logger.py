import logger

def test_log_entry(tmp_path):
    logfile = tmp_path / "log.txt"
    logger.log_entry("test.csv", "created", "dummy file", logfile=logfile)
    text = logfile.read_text()
    assert "test.csv" in text
