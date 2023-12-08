#  Q9a  Fourier transform
import math as cm

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as intg

ki = float(input("Initial value of k ="))
kf = float(input("Final value of k ="))
n = int((kf - ki) / 0.1)

k = ki
x1 = lambda x: x * cm.exp(-(x**2)) * np.cos(k * x) / cm.sqrt(2 * np.pi)
x2 = lambda x: x * cm.exp(-(x**2)) * np.sin(k * x) / cm.sqrt(2 * np.pi)

# x1 = lambda x: cm.exp(-x**2) *np.cos(k*x) /cm.sqrt(2*np.pi)
# x2 = lambda x: cm.exp(-x**2) *np.sin(k*x) /cm.sqrt(2*np.pi)

a = []
b = []
kr = []
for i in range(0, n):
    ai, err = intg.quad(x1, -np.inf, np.inf)
    a.append(ai)
    bi, err = intg.quad(x2, -np.inf, np.inf)
    b.append(bi)
    k += 0.1
    kr.append(k)
a = np.array(a)
b = np.array(b)
kr = np.array(kr)

if np.linalg.norm(a) == 0.0:
    print("Real part of the Fourier Transform is ZERO")
if np.linalg.norm(b) == 0.0:
    print("Imaginary part of the Fourier Transform is ZERO")

# print(a)
plt.plot(kr, a, ".-", label="Real part of the FT")
plt.plot(kr, b, ".-", label="Imaginary part of the FT")
plt.title("Fourier transform(FT) of $x e^{(-a x^2)}$ where $a = 1$")
plt.xlabel("k")
plt.ylim(-0.4, 0.4)
plt.legend()
plt.show()
