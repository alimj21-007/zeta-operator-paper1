# 📘 Summary of Zeta Operator Project

This repository contains the numerical experiments, data, and documentation for the first paper on **zeta-inspired operators** and the computation of their **Hilbert–Schmidt norms**.

---

## 🔎 Overview
- Definition of the zeta operator with kernel \((x+y)^{-s}\).
- Weighted Hilbert space with measure \(x^{\alpha} e^{-\beta x}\).
- Numerical computation of the Hilbert–Schmidt (HS) norm for different grid sizes.
- Convergence analysis and reproducibility focus.

---

## ⚙️ Numerical Setup
Parameters are stored in `data/meta/config.json`:

```json
{
  "s": 1.5,
  "alpha": 0.5,
  "beta": 1.0,
  "grid_size": 200,
  "domain": [0.01, 10],
  "output_path": "data/results/"
}
