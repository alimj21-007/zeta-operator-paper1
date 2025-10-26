import os
import convergence

def test_save_convergence_metrics(tmp_path):
    outfile = tmp_path / "metrics.csv"
    convergence.save_convergence_metrics(outfile)
    assert outfile.exists()

def test_plot_convergence(tmp_path):
    outfile = tmp_path / "plot.png"
    convergence.plot_convergence(outfile)
    assert outfile.exists()
