"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

t, y = np.loadtxt("freefall.csv", delimiter=",", skiprows=1, unpack=True)

v = np.gradient(y, t)
a = np.gradient(v, t)
print("mean a =", a.mean())
print("std a  =", a.std())

v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]
print("max |y_rec - y| =", np.max(np.abs(y_rec - y)))

fig, axs = plt.subplots(3, 1, sharex=True, figsize=(8, 8))

axs[0].plot(t, y)
axs[0].set_ylabel("position y (m)")

axs[1].plot(t, v)
axs[1].set_ylabel("velocity (m/s)")

axs[2].plot(t, a)
axs[2].axhline(-9.81, color="r", linestyle="--", label="-9.81")
axs[2].set_ylabel("acceleration (m/s²)")
axs[2].set_xlabel("time (s)")
axs[2].legend()

plt.tight_layout()
plt.savefig("motion.png", dpi=150)
plt.show()

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?

# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
