import numpy as np
import math
import matplotlib.pyplot as plt


def f(t, x):
    return np.cos(math.pi * t)


t0, x0, h = 0, 0, 0.01
data = 10
t, x = t0, x0  # Euler
T = []
X = []

for i in range(data):
    x += h * f(t, x)
    t += h
    X.append(x)
    T.append(t)

plt.figure(1)
plt.plot(T, X, "-", lw=5, c="red", label="Euler")
plt.legend(loc="best", prop={"size": 16})
plt.title("Comparison between Euler, RK2 method", size=20)

t, x = t0, x0  # RK2 method
X = []

for i in range(data):
    k1 = h * f(t, x)
    k2 = h * f(t + h, x + k1)
    x = x + 0.5 * (k1 + k2)
    t = t + h
    X.append(x)

plt.plot(T, X, "-", lw=4, c="yellow", label="RK2")
plt.legend(loc="best", prop={"size": 16})
plt.show()
