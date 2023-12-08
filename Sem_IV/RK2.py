#  Q1a2  RK2 method
import math

import matplotlib.pyplot as plt
import numpy as np


def f(t, x):
    return np.cos(math.pi * t)


t, x = 0, 0
# Define the step size and number of steps
h = 0.05
n = int((10 - t) / h)

T = []
X = []

for i in range(n):
    k1 = h * f(t, x)
    k2 = h * f(t + h, x + k1)
    x += h * (k1 + k2)
    t += h
    X.append(x)
    T.append(t)

plt.plot(T, X, "-", lw=4, c="c", label="RK2")
plt.legend(loc="best", prop={"size": 16})
plt.show()
