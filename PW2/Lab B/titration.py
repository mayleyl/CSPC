"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

V, pH = np.loadtxt("titration.csv", delimiter=",", skiprows=1, unpack=True)

slope = np.gradient(pH, V)
i = np.argmax(slope)
print("equivalence point at V =", V[i], "mL")

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].plot(V, pH)
axs[0].axvline(V[i], color="r", linestyle="--")
axs[0].set_xlabel("volume of base (mL)")
axs[0].set_ylabel("pH")
axs[0].set_title("Titration curve")

axs[1].plot(V, slope)
axs[1].axvline(V[i], color="r", linestyle="--")
axs[1].set_xlabel("volume of base (mL)")
axs[1].set_ylabel("dpH/dV")
axs[1].set_title("Slope")

plt.tight_layout()
plt.savefig("titration.png", dpi=150)
plt.show()