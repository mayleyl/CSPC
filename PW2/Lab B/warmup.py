"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

def gradient_descent(grad, x0, lr=0.1, n=2000, tol=1e-10):
    x = x0
    for _ in range(n):
        step = lr * grad(x)
        x = x - step
        if abs(step) < tol:
            break
    return x

print("=== 2A: f(x) = (x-3)^2 + 1, x0 = 0 ===")
print("gradient descent:", gradient_descent(df, 0.0))
print("newton          :", newton(df, 0.0, fprime=d2f))
print("SLSQP           :", minimize(lambda x: f(x[0]), x0=[0.0], method="SLSQP").x[0])

# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

for x0 in (0.0, 2.0):
    print(f"\n=== 2B: g(x) = x^4 - 3x^2 + x + 5, x0 = {x0} ===")
    xg = gradient_descent(dg, x0, lr=0.01, n=20000)
    xn = newton(dg, x0, fprime=d2g)
    xs = minimize(lambda x: g(x[0]), x0=[x0], method="SLSQP").x[0]
    print("gradient descent:", xg, " g =", g(xg))
    print("newton          :", xn, " g =", g(xn), " d2g =", d2g(xn),
          "-> minimum" if d2g(xn) > 0 else "-> MAXIMUM")
    print("SLSQP           :", xs, " g =", g(xs))