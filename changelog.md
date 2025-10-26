# Changelog

All notable changes to this project will be documented in this file.  
This project follows **semantic versioning** (MAJOR.MINOR.PATCH).

---

## [0.3.0] - 2025-10-26
### Added
- `summary_table.csv` generation in `main.py`
- Full pipeline logging with `logger.py`
- Documentation pages: `index.md`, `installation.md`, `usage.md`, `modules.md`, `pipeline.md`, `faq.md`, `changelog.md`
- Mermaid and ASCII flowcharts for pipeline visualization

### Changed
- Improved modular structure of `main.py`
- Enhanced reproducibility by centralizing config in `config.json`

---

## [0.2.0] - 2025-10-20
### Added
- `logger.py` module for logging actions to `log.txt`
- Convergence analysis (`convergence.py`) with plots and metrics
- Heatmap visualization (`plots.py`)

### Changed
- Refactored `eigen.py` for cleaner eigenpair computation
- Updated `requirements.txt` with minimal dependencies

---

## [0.1.0] - 2025-10-10
### Added
- Initial project structure (`code/`, `docs/`, `config.json`)
- Core modules: `kernels.py`, `operators.py`, `eigen.py`, `utils.py`
- Basic pipeline in `main.py` for eigenvalue/eigenvector computation
- `requirements.txt` for environment setup

---

## Legend
- **Added** → New features  
- **Changed** → Updates or improvements  
- **Removed** → Features removed  
- **Fixed** → Bug fixes
