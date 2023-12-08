#  Q4  Energy eigs for 1D square using shooting method
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint, simps
from scipy.optimize import bisect


def f(u, x, E):
    y, z = u
    f1, f2 = z, (V - 2*E)*y
    return [f1, f2]

def shoot(E):
    sol = odeint(f, u, x,args = (E, ))
    return sol[:, 0][-1]

V = 0
energies = np.arange(0,100,0.2)
x = np.linspace(-0.5, 0.5, 100)
u = [0, 0.001]

# hits = [shoot(t) for t in energies]
# plt.plot(energies, hits)
# plt.axhline()
Eigen1 = bisect(shoot,0,10)
print("Eigen Energy of Ground state = ", Eigen1)
Eigen2 = bisect(shoot,10,20)
print("Eigen Energy of 1st Excited state = ", Eigen2)

sol1 = odeint(f, u, x, args = (Eigen1, ))
sol2 = odeint(f, u, x, args = (Eigen2, ))

psi1 = sol1[:, 0]
psi2 = sol2[:, 0]

psi1 = psi1/np.sqrt(simps(psi1*psi1, x))
psi2 = psi2/np.sqrt(simps(psi2*psi2, x))

plt.plot(x, psi1, label ="Ground State")
plt.plot(x, psi2,".-",label ="1st excited state")
plt.xlabel("$x$")
plt.ylabel(r"$\psi (x)$")
plt.legend()
plt.title("Wave functions for one dimensional infinite square well ")
plt.show()

plt.plot(x, psi1*psi1, label = "n=1")
plt.plot(x, psi2*psi2, label = 'n=2')
plt.xlabel("$x$")
plt.ylabel(r"$|\psi (x)|^{2}$")
plt.legend()
plt.title("Probability density of ground state(n=1) and 1st excited state(n=2) \nfor one dimensional infinite square well")
plt.show()

