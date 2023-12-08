#  Q4bc  Matrix Inverse by Gauss Seidal method

import numpy as np

R = int(input("Enter the number of equations:"))


print("Enter the coefficients equationwise:")
a = np.array([[float(input()) for _ in range(R)] for _ in range(R)], dtype=float)
p = np.copy(a)

for i in range(0, R - 1):  # determinant of coefficient matrix
    for j in range(i + 1, R):
        factor = p[j, i] / p[i, i]
        p[j, i:R] = p[j, i:R] - factor * p[i, i:R]

det1 = 1.0
for i in range(R):
    det1 *= p[i, i]
print("Determinant of the given coefficient matrix = ", det1)

b = np.identity(R)

print("Enter the guess values of the elements of inverse matrix: ")
x = np.array([[float(input()) for _ in range(R)] for _ in range(R)], dtype=float)

err = 1.0
factor = np.zeros((R, R))

while err > 0.00001:  # Calculation of Inverse
    xold = np.copy(x)
    for i in range(R):
        for j in range(R):
            for k in range(R):
                if k != i:
                    factor[i, j] += a[i, k] * x[k, j]

    for i in range(R):
        for j in range(R):
            x[i, j] = (b[i, j] - factor[i, j]) / a[i, i]
            factor[i, j] = 0.0
    err = np.linalg.norm(xold - x)

print("The inverse of the given coefficient matrix is:")
print(x)

y = np.copy(x)
for i in range(0, R - 1):  # determinant of inverse
    for j in range(i + 1, R):
        factor = y[j, i] / y[i, i]
        y[j, i:R] = y[j, i:R] - factor * y[i, i:R]

det2 = 1.0
for i in range(R):
    det2 *= y[i, i]
print("Determinant of inverse matrix = ", det2)
print("inverse of determinant of coefficient matrix =", 1 / det1)
