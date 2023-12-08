#  Q1a4  Comparsion between Euler, RK2 & Rk4 method
import math

import matplotlib.pyplot as plt
import numpy as np


def f(t, x):
    return np.cos(math.pi * t)


t0, x0 = 0, 0
# Define the step size and number of steps
h = 0.05
n = int((10 - t0) / h)

t, x = t0, x0  # Euler
T = []
X = []
for i in range(n):
    x += h * f(t, x)
    t += h
    X.append(x)
    T.append(t)
plt.figure(1)
plt.plot(T, X, "-", lw=4, c="m", label="Euler")
plt.legend(loc="best", prop={"size": 16})

t, x = t0, x0  # RK4 method
X = []
for i in range(n):
    a = h * f(t, x)
    b = h * f(t + 0.5 * h, x + 0.5 * a)
    c = h * f(t + 0.5 * h, x + 0.5 * b)
    d = h * f(t + h, x + c)
    x = x + (a + 2 * b + 2 * c + d) / 6
    t += h
    X.append(x)
plt.figure(1)
plt.plot(T, X, "-", lw=4, c="b", label="RK4")
plt.legend(loc="best", prop={"size": 16})

t, x = t0, x0  # RK2 method
X = []
for i in range(n):
    k1 = h * f(t, x)
    k2 = h * f(t + h, x + k1)
    x = x + 0.5 * (k1 + k2)
    t = t + h
    X.append(x)
plt.figure(1)
plt.plot(T, X, "-", lw=4, c="c", label="RK2")
plt.legend(loc="best", prop={"size": 16})

plt.title("Comparsion between Euler, RK2 & Rk4 method", size=18)
plt.show()
