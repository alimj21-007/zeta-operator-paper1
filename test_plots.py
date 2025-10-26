import os
import plots

def test_plot_heatmap(tmp_path):
    outfile = tmp_path / "heatmap.png"
    plots.plot_heatmap(grid_size=5, s=0.5, domain=(0,1), output_file=outfile)
    assert outfile.exists()
