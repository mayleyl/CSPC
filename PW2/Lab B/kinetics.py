"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

t, C = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1, unpack=True)
C0 = C[0]

def error(k):
    return np.sum((C - C0 * np.exp(-k * t))**2)

res = minimize(lambda p: error(p[0]), x0=[0.5], method="SLSQP", bounds=[(0, 5)])
k_fit = res.x[0]
print("fitted k =", k_fit)

tt = np.linspace(t.min(), t.max(), 200)
plt.plot(t, C, "o", label="data")
plt.plot(tt, C0 * np.exp(-k_fit * tt), "-", label=f"fit, k = {k_fit:.3f}")
plt.xlabel("time")
plt.ylabel("concentration")
plt.legend()
plt.savefig("kinetics.png", dpi=150)
plt.show()