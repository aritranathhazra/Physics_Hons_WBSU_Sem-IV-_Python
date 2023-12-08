#  Q7a  Laplace equation in 2D
import matplotlib.pyplot as plt
import numpy as np

N = 100
iter = 10000
v = np.zeros((N, N))
for k in range(N):
    v[0, k] = 10.0
E = []
Niter = range(iter)

for iter in Niter:
    v0 = v.copy()
    v[1:-1, 1:-1] = 0.25 * (v[:-2, 1:-1] + v[2:, 1:-1] + v[1:-1, :-2] + v[1:-1, 2:])
    err = np.sum((v - v0) ** 2)
    E.append(err)


x = range(0, N, 2)
y = range(0, N, 2)
X, Y = np.meshgrid(x, y)
Z = v[X, Y]

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.contour3D(X, Y, Z, 100, cmap="viridis")
plt.title("Slution of Laplace's equation after 1000 iterations")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
