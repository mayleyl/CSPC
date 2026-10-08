# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup

Create the environment for a given lab:

conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- Created the CSPC repository with Git and GitHub.
- Added the PW1/Lab A structure, conda environment, radioactive decay simulation, tests, and speed comparison.

**Speed comparison (loop vs NumPy):**
- loop : 2.750563 s
- numpy : 0.000282 s
- speed-up: 9753.42 x faster

**Tests:** all passing? yes

**Conclusion:**
- I learned how to use Git and GitHub, create a reproducible conda environment, and write tests for a simulation. The NumPy version was much faster than the pure-Python loop. I also learned that tests can help find problems in the code and confirm that the simulation works as expected.


## PW1 — Lab B

The observed decay data were compared with the analytical decay law:
N(t) = N0 * exp(-λt)
where λ = 0.3 and N0 is the first observed value.
The observed data and the analytical curve show the decay behavior of the system.
Snakemake was used to automate the workflow. It takes `decay_observed.csv` as input and runs `plot.py` to produce `figure.png`. If the output file is already up to date, Snakemake does not run the rule again.


## PW2 — Lab A

- **Mean acceleration:** -8.58 m/s² (expected about -9.81 for free fall); std = 28.7 m/s².
- **Why the acceleration is noisy:** differentiation compares neighbouring
  measurements, so it amplifies noise; the acceleration comes from two
  derivatives, so its noise is much larger than the noise in the position.
- **Integrating back:** the position recovered by integrating the noisy
  acceleration differs from the original by at most 0.78 m, because
  integration is a sum and random noise partly cancels out.

  - **Bonus (2D trajectory):** computed speed from np.gradient of x and y
  separately; see trajectory.png.


  ## PW2 — Lab B

- **Methods (Part 2):** On the convex function f(x) = (x-3)^2 + 1 all three
  methods (gradient descent, Newton, SLSQP) agree and reach x = 3. On
  g(x) = x^4 - 3x^2 + x + 5 they do not. From x0 = 0, gradient descent and
  SLSQP found the global minimum (x = -1.30, g = 1.486), but Newton converged to
  x = 0.170, where g'' = -5.65 < 0, i.e. a maximum, not a minimum (Newton only
  solves g'(x) = 0 and does not distinguish minima from maxima). From x0 = 2,
  gradient descent and Newton found the local minimum x = 1.131 (g = 3.93),
  while SLSQP found the global minimum x = -1.30. So on a complicated landscape
  both the starting point and the algorithm determine which stationary point
  is reached.
- **Fitted rate constant:** k = 0.262 (expected about 0.25).
- **Equilibrium (K = 15.6):** Newton (root-finding) and SLSQP (minimising
  k_imbalance^2) agree: x = 0.664. Equilibrium composition:
  n(H2) = n(I2) = 0.336 mol, n(HI) = 1.328 mol.
  - **Titration (bonus):** the equivalence point is at V = 50.0 mL, where the
  slope of the pH curve (np.gradient) is largest.