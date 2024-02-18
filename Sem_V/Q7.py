#  Q7  Schrödinger equation with Coulomb potential
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps


def u(x):
    return -2 / x


n = 2000  # Number of intervals
dim = n - 1  # Number of internal points
xl = 0  # xl corresponds to origin
xr = 200.0
delta = (xr - xl) / n

x = np.linspace(xl + delta, xr - delta, dim)

# Fill Hamiltonian
h = np.zeros((dim, dim), float)
for i in range(len(h) - 1):
    h[i, i + 1] = h[i + 1, i] = -1 / delta**2

for i in range(len(h)):
    h[i, i] = 2.0 / delta**2 + u(x[i])

vals, vecs = np.linalg.eigh(h)
z = np.argsort(vals)
z = z[0:2]
energy = vals[z]

print("Ground state energy eigen value = ", energy[0])
print("1st excited state energy eigen value = ", energy[1])

for i in range(len(z)):
    y = []
    y = np.append(y, -vecs[:, z[i]])
    Nor = np.sqrt(simps(y * y, x))
    y = y / Nor
    if i == 0:
        plt.plot(x, y, label="Ground state")
    else:
        plt.plot(x, y, "-.", label="1st excited state")
plt.xlim(0, 15)
plt.xlabel("$r$")
plt.ylabel("$r R_{nl}(r)$")
plt.legend()
plt.title("Wave functions for s-wave (hydrogen atom)")
plt.show()

for i in range(len(z)):
    p = []
    p = np.append(p, vecs[:, z[i]] * vecs[:, z[i]])
    Nor = simps(p, x)
    p = p / Nor
    if i == 0:
        plt.plot(x, p, label="Ground state")
    else:
        plt.plot(x, p, "-.", label="1st excited state")
plt.xlim(0, 15)
plt.xlabel("$r$")
plt.ylabel("$|r R_{nl}(r)|^2$")
plt.legend()
plt.title(
    "Probability density of ground state and 1st excited state \n s-wave of hydrogen atom"
)
plt.show()
