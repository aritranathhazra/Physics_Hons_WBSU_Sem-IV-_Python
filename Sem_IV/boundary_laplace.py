import numpy as np
import matplotlib.pyplot as plt

N = 100
iter = 10000
v = np.zeros((N, N))
for k in range(N):
    v[0, k] = 10.0
E = []
Niter = range(iter)

# for iter in Niter:
#     v0 = v.copy()
#     for i in range(1, N -1):
#         for j in range(1, N -1):
#             v[i,j] = 0.25*(v[i+1,j]+ v[i-1, j] + v[i, j+1] + v[i, j-1])
#     err = np.sum((v - v0)**2)
#     E.append(err)

for iter in Niter:
    v0 = v.copy()
    v[1:-1, 1:-1] = 0.25 * (v[:-2, 1:-1] + v[2:, 1:-1] + v[1:-1, :-2] + v[1:-1, 2:])
    err = np.sum((v - v0) ** 2)
    E.append(err)


from mpl_toolkits.mplot3d import Axes3D

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
