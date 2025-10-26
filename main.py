"""
main.py
-------
Main pipeline script for the zeta-inspired operator project.
Loads configuration, computes eigenpairs, generates plots,
saves outputs, logs all actions, and creates a summary table.
"""

from utils import load_config, save_csv
from eigen import compute_eigenpairs
from convergence import plot_convergence, save_convergence_metrics
from plots import plot_heatmap
from logger import log_entry

def main():
    # Load configuration
    config = load_config("../config.json")
    grid_size = config["grid_size"]
    s = config["s"]
    domain = config["domain"]
    num_eigs = config["num_eigenpairs"]

    summary_rows = []

    # === Eigenpairs ===
    eigs, vecs = compute_eigenpairs(grid_size, s, domain, num_eigs)
    save_csv(config["output_files"]["eigenvalues"], ["eigenvalue"],
             [[f"{val:.6f}"] for val in eigs])
    save_csv(config["output_files"]["eigenvectors"],
             [f"v{i+1}" for i in range(num_eigs)],
             [[f"{val:.6f}" for val in row] for row in vecs])
    log_entry("eigenvalues.csv", "created", "Eigenvalues computed and saved")
    log_entry("eigenvectors.csv", "created", "Eigenvectors computed and saved")
    summary_rows.append(["eigenvalues.csv", "CSV", "Top eigenvalues of operator"])
    summary_rows.append(["eigenvectors.csv", "CSV", "Corresponding eigenvectors"])

    # === Convergence ===
    plot_convergence(config["output_files"]["convergence_plot"])
    save_convergence_metrics(config["output_files"]["convergence_metrics"])
    log_entry("convergence_plot.png", "created", "Convergence plot generated")
    log_entry("convergence_metrics.csv", "created", "Convergence metrics saved")
    summary_rows.append(["convergence_plot.png", "PNG", "Convergence of Trace and HS norm"])
    summary_rows.append(["convergence_metrics.csv", "CSV", "Trace and HS norm values"])

    # === Heatmap ===
    plot_heatmap(grid_size, s, domain, config["output_files"]["heatmap_kernel"])
    log_entry("heatmap_kernel.png", "created", "Kernel heatmap generated")
    summary_rows.append(["heatmap_kernel.png", "PNG", "Heatmap of kernel matrix"])

    # === Summary Table ===
    save_csv("summary_table.csv", ["filename", "type", "description"], summary_rows)
    log_entry("summary_table.csv", "created", "Summary of all generated outputs")

    # === Final Log ===
    log_entry("main.py", "executed", "Full pipeline completed successfully")

if __name__ == "__main__":
    main()
