# Pipeline Execution Flow

This document explains the execution flow of `main.py` in the **Zeta Operator Project**.  
The pipeline is modular and ensures reproducibility, visualization, and logging at every step.

---

## 🔄 Step-by-Step Execution

1. **Load Configuration**
   - Reads parameters from `config.json`
   - Includes grid size, domain, parameter `s`, and number of eigenpairs

2. **Compute Eigenpairs**
   - Uses `eigen.py` to compute eigenvalues and eigenvectors
   - Saves results into:
     - `eigenvalues.csv`
     - `eigenvectors.csv`

3. **Convergence Analysis**
   - Generates convergence plot (`convergence_plot.png`)
   - Saves convergence metrics (`convergence_metrics.csv`)
   - Ensures numerical stability

4. **Kernel Heatmap**
   - Creates a heatmap visualization of the kernel matrix (`heatmap_kernel.png`)

5. **Summary Table**
   - Collects all outputs into `summary_table.csv`
   - Provides filename, type, and description

6. **Logging**
   - Every action is recorded in `log.txt`
   - Ensures reproducibility and traceability

---

## 📊 Mermaid Flowchart

```mermaid
flowchart TD

    A[Start main.py] --> B[Load config.json]
    B --> C[Compute eigenpairs]
    C --> C1[Save eigenvalues.csv]
    C --> C2[Save eigenvectors.csv]
    C1 --> D[Log actions]
    C2 --> D

    D --> E[Generate convergence plot]
    E --> E1[Save convergence_plot.png]
    E --> E2[Save convergence_metrics.csv]
    E1 --> F[Log actions]
    E2 --> F

    F --> G[Generate kernel heatmap]
    G --> G1[Save heatmap_kernel.png]
    G1 --> H[Log actions]

    H --> I[Create summary_table.csv]
    I --> J[Log summary]

    J --> K[Pipeline completed successfully]
