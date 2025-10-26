# Installation Guide

This document explains how to set up the environment for the **Zeta Operator Project**.

---

## ✅ Prerequisites

- Python **3.10+**
- Git (for cloning the repository)
- A terminal or command prompt

---

## 📥 Step 1: Clone the Repository

```bash
git clone https://github.com/alimj21-007/zeta-operator-paper.git
cd zeta-operator-paper
paper

## 🛠 Step 2: Create a Virtual Environment (Recommended)

On Linux / macOS:
python3 -m venv venv
source venv/bin/activate
On Windows (PowerShell):
python -m venv venv
venv\Scripts\activate

## 📦 Step 3: Install Dependencies

All required Python packages are listed in requirements.txt.

pip install -r requirements.txt

This will install:

NumPy → numerical computations

Matplotlib → plotting and visualization

## 🚀 Step 4: Verify Installation

Run the following command to check that everything works:

cd code
python main.py

If successful, the pipeline will:
Compute eigenvalues and eigenvectors
Generate convergence plots and metrics
Create a kernel heatmap
Save all outputs in CSV/PNG format
Log actions in log.txt

🎉 You’re Ready!

Your environment is now set up. Continue to the Usage Guide to learn how to run experiments and interpret results.
