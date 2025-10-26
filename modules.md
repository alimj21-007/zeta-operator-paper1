# Modules Overview

This document describes each Python module in the `code/` directory, its purpose, key functions, and how it fits into the pipeline.

---

## 🔹 kernels.py
**Purpose:**  
Defines kernel functions used to build integral operators.

**Key Functions:**
- `zeta_kernel(x, y, s)` → Zeta-inspired kernel  
- `gaussian_kernel(x, y, sigma)` → Gaussian kernel  
- `exponential_kernel(x, y, alpha)` → Exponential kernel  

**Role in Pipeline:**  
Provides the mathematical building blocks for constructing operators.

---

## 🔹 operators.py
**Purpose:**  
Constructs operators from kernels and discretizes them for numerical analysis.

**Key Functions:**
- `build_operator(kernel, grid_size, domain)` → Builds the operator matrix  
- `apply_operator(operator, vector)` → Applies operator to a vector  

**Role in Pipeline:**  
Transforms kernel definitions into usable operator matrices.

---

## 🔹 eigen.py
**Purpose:**  
Computes eigenvalues and eigenvectors of operators.

**Key Functions:**
- `compute_eigenpairs(grid_size, s, domain, num_eigs)` → Returns eigenvalues and eigenvectors  

**Role in Pipeline:**  
Provides spectral data (eigenvalues/eigenvectors) for analysis.

---

## 🔹 convergence.py
**Purpose:**  
Analyzes convergence of operator metrics.

**Key Functions:**
- `plot_convergence(output_file)` → Generates convergence plot  
- `save_convergence_metrics(output_file)` → Saves trace and Hilbert–Schmidt norm values  

**Role in Pipeline:**  
Ensures numerical stability and validates results.

---

## 🔹 plots.py
**Purpose:**  
Generates visualizations of operators and kernels.

**Key Functions:**
- `plot_heatmap(grid_size, s, domain, output_file)` → Heatmap of kernel matrix  

**Role in Pipeline:**  
Provides visual intuition about operator structure.

---

## 🔹 utils.py
**Purpose:**  
Utility functions for configuration and file handling.

**Key Functions:**
- `load_config(path)` → Loads parameters from `config.json`  
- `save_csv(filename, headers, rows)` → Saves tabular data to CSV  

**Role in Pipeline:**  
Handles I/O and configuration management.

---

## 🔹 logger.py
**Purpose:**  
Records all actions and outputs in a log file.

**Key Functions:**
- `log_entry(filename, action, description, logfile="log.txt")` → Appends a log entry  

**Role in Pipeline:**  
Provides reproducibility and a history of generated outputs.

---

## 🔹 main.py
**Purpose:**  
Orchestrates the entire pipeline.

**Key Steps:**
1. Load configuration  
2. Compute eigenpairs  
3. Generate convergence plots and metrics  
4. Create kernel heatmap  
5. Save summary table  
6. Log all actions  

**Role in Pipeline:**  
Acts as the central controller that ties all modules together.
