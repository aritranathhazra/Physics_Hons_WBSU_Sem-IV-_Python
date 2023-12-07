import numpy as np
import matplotlib.pyplot as plt

n = int(input(" enter the time step needed "))

x = np.zeros((181))
u = np.zeros((181, n + 2))

# initial condition:-(here it is '1st excited state')
x[:] = np.array([i * np.pi / 180 for i in range(181)])
u[:, 0] = np.sin(x)

for j in range(0, n + 1):
    for i in range(1, 180):
        if j == 0:
            u[i, j + 1] = u[i + 1, j] + u[i - 1, j] - (u[i + 1, j] + u[i - 1, j]) / 2
        else:
            u[i, j + 1] = u[i + 1, j] + u[i - 1, j] - u[i, j - 1]

# for j in range(0,n+1):
#    if j==0:
#        u[1:-1,j+1]=u[:-2,j+1]+u[2:,j]-(u[:-2,j]+u[2:,j])/2
#    else:
#        u[1:-1,j+1]= (u[:-2,j]+u[2:,j]-u[1:-1,j-1])

s = np.zeros(181)

s[:] = u[:, n - 2]

plt.plot(np.sin(x), ".-", label="Initial configuration")
plt.plot(s, "--", label="after timestep = 70")
plt.title("Profile of wave on a string fixed at two ends")
plt.xlabel("Position on string")
plt.ylabel("Amplitude of wave on a string")
plt.ylim(0.0, 1.5)
plt.legend()
plt.show()

# -------------------input----------------------
# enter the time step needed 70
# ----------------------------------------------
