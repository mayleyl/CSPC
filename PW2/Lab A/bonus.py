import numpy as np
import matplotlib.pyplot as plt

t, x, y = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1, unpack=True)

vx = np.gradient(x, t)
vy = np.gradient(y, t)
speed = np.sqrt(vx**2 + vy**2)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].plot(x, y)
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")
axs[0].set_title("Path")

axs[1].plot(t, speed)
axs[1].set_xlabel("time (s)")
axs[1].set_ylabel("speed")
axs[1].set_title("Speed")

plt.tight_layout()
plt.savefig("trajectory.png", dpi=150)
plt.show()