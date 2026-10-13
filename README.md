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



  ## PW3 — Data, Distributions, Testing, and Causation

**Data.** Heart Disease Cleveland, Kaggle dataset by ritwikb3
(https://www.kaggle.com/datasets/ritwikb3/heart-disease-cleveland), based on the
UCI Heart Disease dataset: Janosi, A., Steinbrunn, W., Pfisterer, M., &
Detrano, R. (1989). UCI Machine Learning Repository.
https://doi.org/10.24432/C52P4X. 303 patients, no missing values,
target = 1 means heart disease. The chemical-exposure data is
chemicals_cancer.csv (1000 synthetic patients).

### Session 1 — distributions and normality

**Shapes** (distributions.png):
- **age:** a wide, roughly bell-shaped hill peaking around 58-60 years, slightly
  uneven and a little skewed to the left (fewer young patients than old ones).
- **chol:** peak around 200-250 with a long right tail; one patient lies far
  from the rest (about 560 mg/dl), an outlier.
- **trestbps:** peak around 120-140 with a right tail up to 200. The histogram
  is jagged because blood pressure is usually recorded as round numbers
  (120, 130, 140).
- **thalach:** peak around 160 with a long tail to the left down to about 70, so
  it is skewed to the left.

**Normality verdicts** (qqplots.png, Shapiro-Wilk test, skewness). I used both a
graphical check and a statistical test, because with n = 303 the Shapiro test
is very sensitive and rejects normality even for small deviations, so I did not
rely on the p-value alone.
- **age:** Shapiro p = 0.006, skew = -0.21. Q-Q points lie almost on the line,
  with deviations only at the extreme ends -> **approximately normal**.
- **chol:** p = 6e-9, skew = 1.13. Q-Q points curve upward at the right end and
  the top point (the outlier) is far from the line -> **not normal** (strong
  right skew).
- **trestbps:** p = 2e-6, skew = 0.70. Q-Q plot shows steps (rounded values) and
  an upward bend on the right -> **not normal**.
- **thalach:** p = 7e-5, skew = -0.53. Q-Q points fall below the line at the
  left end, i.e. too many low values for a normal law -> **not normal**
  (left skew).

### Session 2

- **Heart rate by group.** thalach is not normal overall, and in the healthy
  group Shapiro p = 0.0005 (in the disease group p = 0.35), so I used the
  non-parametric Mann-Whitney U test, which does not assume normality
  (U = 5806.5, p = 1.9e-13). Welch's t-test gives the same conclusion
  (t = -7.86, p = 9e-14). Patients with heart disease reach a lower maximum
  heart rate: the two groups genuinely differ.
- **Uncertainty on the means.** Disease: mean 139.3 bpm, SEM 1.92 (n = 139).
  Healthy: mean 158.4 bpm, SEM 1.50 (n = 164). In thalach_means.png the error
  bars are far apart and do not overlap, so the picture agrees with the test.
- **Age vs thalach.** Pearson r = -0.39 and Spearman rho = -0.39 (p ~ 1e-12): a
  moderate negative relationship; maximum heart rate tends to decrease with age
  (age_thalach.png).
- **Bonus.** target proportions are 54% (no disease) and 46% (disease); entropy
  = 0.995 bits (the maximum for two classes is 1). The column is almost
  perfectly balanced, so it is about as hard to guess as a fair coin.

### Chemical mystery

- **Naive analysis.** Correlation with malignancy: cadmium r = 0.88, benzene
  r = 0.38. At face value, cadmium looks like the cause.
- **Accounting for pollution_index.** Cadmium is almost the same variable as
  pollution_index (r = 0.98), and pollution is itself strongly tied to
  malignancy, so it could be a confounder. I restricted the data to narrow
  pollution bands (patients with similar pollution) and recomputed the
  correlations. Cadmium's association drops (r = 0.29 for pollution 0-20, 0.32
  for 40-60, 0.18 for 80-100), while benzene's stays at about 0.68-0.71 in
  every band (chemicals.png).
- **Conclusion.** Benzene is the real cause of malignancy. Cadmium only looked
  guilty because it tracks pollution, a third variable that influences both.
  Within a fixed level of pollution cadmium has much less relationship to
  malignancy, whereas benzene's effect does not go away.