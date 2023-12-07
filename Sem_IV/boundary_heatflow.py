import numpy as np
import matplotlib.pyplot as plt


c = np.linspace(0, 1, 101)
u = np.exp(-((c) ** 2) / 0.001)  # continuous heat at end point x=0

for time in range(1000):
    u[1:-1] += 0.25 * (u[2:] - 2 * u[1:-1] + u[:-2])

plt.plot(c, u, ".-", label="for time = 1000")
plt.plot(c, np.exp(-((c) ** 2) / 0.001), "--", label="for time = 0")
plt.title("Profile of heat flow in 1-D for two different times")
plt.xlabel("Position")
plt.ylabel("Intensity of heat energy")
plt.legend()
plt.show()
