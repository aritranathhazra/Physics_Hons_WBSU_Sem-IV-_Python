# Solution by Gauss Seidal method( Guidelines 4(a))

import numpy as np

R = int(input("Enter the number of equations:"))

print("Enter the coefficients equationwise:")
a = np.array([[float(input()) for i in range(R)] for j in range(R)])

print("Enter the r.h.s constant numbers equationwise: ")
b = np.array([float(input()) for i in range(R)])

print("Enter the guess values of the variables: ")
x = np.array([float(input()) for i in range(R)])

err = 1.0
factor = 0.0

while err > 0.001:
    xold = np.copy(x)
    for i in range(R):
        for j in range(R):
            if i != j:
                factor += a[i, j] * x[j]
        x[i] = (b[i] - factor) / a[i, i]
        factor = 0.0
    err = np.linalg.norm(xold - x)

print("The unknown variables are:")
for i in range(R):
    print("X", i, "=", x[i])
