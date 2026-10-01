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