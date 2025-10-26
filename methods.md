# Methods

## Kernel Definitions
We implemented several kernels:
- **Zeta kernel**: motivated by analytic continuation of ζ(s)
- **Gaussian kernel**: for stability and comparison
- **Exponential kernel**: as a test case for decay properties

## Operator Construction
Operators are built by discretizing integral transforms of the form:
\[
(Tf)(x) = \int K(x,y) f(y) \, dy
\]

## Eigenvalue Computation
We compute eigenpairs using numerical linear algebra routines, storing results in CSV format.

## Convergence Metrics
Two metrics are tracked:
- **Trace norm**
- **Hilbert–Schmidt norm**

## Visualization
- Heatmaps of kernel matrices
- Convergence plots across grid sizes
