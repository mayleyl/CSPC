"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

def k_imbalance(x):
    return (2*x)**2 / ((a - x) * (b - x)) - K

# Method 1: root-finding with Newton
x_newton = newton(k_imbalance, 0.5)

# Method 2: minimise k_imbalance(x)^2 with SLSQP
res = minimize(lambda x: k_imbalance(x[0])**2, x0=[0.5],
               method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res.x[0]

print("Newton x =", x_newton)
print("SLSQP  x =", x_slsqp)

x_eq = x_newton
print(f"n(H2) = {a - x_eq:.4f} mol")
print(f"n(I2) = {b - x_eq:.4f} mol")
print(f"n(HI) = {2 * x_eq:.4f} mol")

# Plot amounts vs extent
x = np.linspace(0, 0.99, 300)
plt.plot(x, a - x, label="H2")
plt.plot(x, b - x, "--", label="I2")
plt.plot(x, 2 * x, label="HI")
plt.axvline(x_eq, color="k", linestyle=":", label=f"equilibrium x = {x_eq:.3f}")
plt.xlabel("extent x")
plt.ylabel("amount (mol)")
plt.legend()
plt.savefig("equilibrium.png", dpi=150)
plt.show()