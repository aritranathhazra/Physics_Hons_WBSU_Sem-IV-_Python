#  Q1  Spin within a magnetic field
import matplotlib.pyplot as plt
import numpy as np


def U(t):
    Evolution = np.array(
        [
            [np.exp(-1j * t * (H_d[0, 0] / h_bar)), 0],
            [0, np.exp(-1j * t * (H_d[1, 1] / h_bar))],
        ]
    )
    return Evolution


t = 0
g = 0.1
B = 0.1
h_bar = 1
S_x = (h_bar / 2) * np.array([[0, 1], [1, 0]])  # S_x matrix
H = g * S_x * B  # interaction Hamiltonian

egvl, egvc = np.linalg.eig(H)  # Eigenvalue & Eigenvectors of H

# diagonalisation of H by similarity transformation
# means interaction Hamiltonian H_d is in the eigen vectors of S_x
H_d = np.dot(egvc.conj().T, np.dot(H, egvc))

# Initial State (Spin up of S_z in the eigen vectors of S_x)
I1 = np.array([1, 1]) / np.sqrt(2)
# Initial State (Spin down of S_z in the eigen vectors of S_x)
I2 = np.array([1, -1]) / np.sqrt(2)
Result = []
for i in range(0, 5000):
    F = np.dot(U(t), I1)  # Final state (After evolution)
    P = np.dot(I1, F)
    abs_P = np.abs(P)  # Absolute value of P
    Result.append(abs_P**2)
    t += 0.5

Result = np.array(Result)

plt.plot(Result)
plt.title("Probability of getting Spin UP(along z axis) state with time")
plt.xlabel(r"time(in $\omega^{-1}$, where $\omega = gB$)")
plt.ylabel("Probability")
plt.xlim(0.0, 5000)
plt.show()
