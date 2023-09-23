import numpy as np
import math
import matplotlib.pyplot as plt

def f(t, x):
    return np.cos(math.pi * t)

t0, x0, h = 0, 0, 0.05
data = 10
t, x = t0, x0

T = []
X_euler = []
X_rk4 = []

for i in range(data):
    # Euler's method
    x += h * f(t, x)
    t += h
    X_euler.append(x)
    T.append(t)

t, x = t0, x0

for i in range(data):
    # RK4 method
    a = h * f(t, x)
    b = h * f(t + 0.5 * h, x + 0.5 * a)
    c = h * f(t + 0.5 * h, x + 0.5 * b)
    d = h * f(t + h, x + c)
    x = x + (a + 2 * b + 2 * c + d) / 6
    t += h
    X_rk4.append(x)

plt.figure(1)
plt.plot(T, X_euler, '-', lw=4, c='m', label='Euler')
plt.plot(T, X_rk4, '-', lw=4, c='b', label='RK4')
plt.legend(loc='best', prop={'size': 16})
plt.title('Comparison between Euler and RK4 method', size=18)
plt.show()
