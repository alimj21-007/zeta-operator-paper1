# Usage Guide

This document explains how to run the **Zeta Operator Project** pipeline and interpret its outputs.

---

## 🚀 Running the Pipeline

After completing the [Installation](installation.md) steps:

```bash
cd code
python main.py

The script will:

Load configuration from config.json

Compute eigenvalues and eigenvectors

Generate convergence plots and metrics

Create a kernel heatmap

Save all outputs in CSV/PNG format

Log every action in log.txt

📂 Generated Outputs

1. eigenvalues.csv

Contains the computed eigenvalues of the operator.

Each row corresponds to one eigenvalue.

Useful for spectral analysis and comparisons.

2. eigenvectors.csv

Contains the eigenvectors associated with the eigenvalues.

Each column corresponds to one eigenvector.

Can be used for visualization or further numerical experiments.

3. convergence_plot.png

A plot showing convergence of trace and Hilbert–Schmidt norm.

Helps verify numerical stability and accuracy.

4. convergence_metrics.csv

Tabular data of convergence metrics.

Includes values of trace and HS norm at different grid sizes.

5. heatmap_kernel.png

Heatmap visualization of the kernel matrix.

Provides intuition about the operator’s structure.

6. summary_table.csv

A summary of all generated outputs.

Columns: filename, type, description.

Acts as a quick reference for all results.

📝 Log File

log.txt

Records every action performed by the pipeline.

Each entry includes:

[timestamp] filename - action - description

Example:

[2025-10-26T15:45:00] eigenvalues.csv - created - Eigenvalues computed and saved

This file ensures reproducibility and provides a history of all generated outputs.

✅ Next Steps

Explore the Modules section for details on each component.

Review the Pipeline page for a visual flowchart of execution.

Check FAQ for troubleshooting and common questions.

