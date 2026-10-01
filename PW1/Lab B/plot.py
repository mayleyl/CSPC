"""
PW1 Lab B -- read observed decay data and compare it to the analytical law.
Produce a 1x2 figure:  left = observed data,  right = analytical N0*exp(-lam*t),
with SHARED axes so the two shapes are directly comparable.

Complete the TODOs below. Run with:  python plot.py
"""

import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3     # decay constant, given

# TODO 1: read decay_observed.csv
data = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1)

t = data[:, 0]
observed = data[:, 1]

# TODO 2: set N0 to the FIRST observed value
N0 = observed[0]

analytical = N0 * np.exp(-LAMBDA * t)

# TODO 3: make a 1x2 subplot with SHARED x and y axes
fig, ax = plt.subplots(1, 2, sharex=True, sharey=True)

ax[0].scatter(t, observed)
ax[0].set_title("Observed data")
ax[0].set_xlabel("Time")
ax[0].set_ylabel("Count")

ax[1].plot(t, analytical)
ax[1].set_title("Analytical")
ax[1].set_xlabel("Time")
ax[1].set_ylabel("Count")

plt.tight_layout()

# TODO 4: save the figure as figure.png
plt.savefig("figure.png")