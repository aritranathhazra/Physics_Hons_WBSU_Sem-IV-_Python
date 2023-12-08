#  Q1a3  RK4 method
import math

import matplotlib.pyplot as plt
import numpy as np


def f(t, x):
    return np.cos(math.pi * t)


t , x = 0, 0
# Define the step size and number of steps
h = 0.05
n = int((10 - t) / h)


T = []
X = []

for i in range(n):
    a = h * f(t, x)
    b = h * f(t + 0.5 * h, x + 0.5 * a)
    c = h * f(t + 0.5 * h, x + 0.5 * b)
    d = h * f(t + h, x + c)
    x = x + (a + 2 * b + 2 * c + d) / 6
    t += h
    X.append(x)
    T.append(t)

plt.figure(1)
plt.plot(T, X, "-", lw=4, c="b", label="RK4")
plt.legend(loc="best", prop={"size": 16})
plt.show()
