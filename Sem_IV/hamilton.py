#  Q1c  Hamilton's eqn of 1D motion when attached with string
import matplotlib.pyplot as plt
import numpy as np


def f(t, x, z):
    return z


def g(t, x, z):
    return -((np.pi) ** 2) * x


t0, x0, z0, h = 0.0, 1.0, 0.0, 0.05
ini_time = 0.0
fin_time = 10.0
n = int((fin_time - ini_time) / h)
print("n=", n)
t, x, z = t0, x0, z0
T = []
X = []
Z = []
for i in range(n):
    x = h * f(t, x, z)
    z = h * g(t, x, z)
    t = h
    X.append(x)
    T.append(t)
    Z.append(z)
x, t, z = x0, t0, z0
X1 = []
Z1 = []
T1 = []
for i in range(n):
    k1 = h * f(t, x, z)
    l1 = h * g(t, x, z)
    k2 = h * f(t + 0.5 * h, x + 0.5 * k1, z + 0.5 * l1)
    l2 = h * g(t + 0.5 * h, x + 0.5 * k1, z + 0.5 * l1)
    k3 = h * f(t + 0.5 * h, x + 0.5 * k1, z + 0.5 * l2)
    l3 = h * g(t + 0.5 * h, x + 0.5 * k1, z + 0.5 * l2)
    k4 = h * f(t + h, x + k3, z + l3)
    l4 = h * g(t + h, x + k3, z + l3)
    x += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    z += (l1 + 2 * l2 + 2 * l3 + l4) / 6
    z += (l1 + 2 * l2 + 2 * l3 + l4) / 6
    X1.append(x)
    Z1.append(z)
    T1.append(t)
plt.title("Phase Space Plot", size=20)
plt.plot(X, Z, "-", label="Euler Method")
plt.plot(X1, Z1, "-", label="RK4 Method")
plt.legend()
plt.show()


# output
# n= 200
