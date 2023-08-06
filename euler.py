import matplotlib.pyplot as plt
import numpy as np

# Define the differential equation to solve
def f(t, y):
    return -y+t**2+2*t+4

# Define the initial conditions
t0 = 0
y0 = 0.5

# Define the step size and number of steps
h = 0.1
n = 100

# Initialize arrays for t and y values
t = np.zeros(n+1)
y = np.zeros(n+1)

# Set initial values
t[0] = t0
y[0] = y0

# Solve the ODE using the Euler method
for i in range(n):
    t[i+1] = t[i] + h
    y[i+1] = y[i] + h * f(t[i], y[i])

# Write the results to a file
with open('euler.dat', 'w') as f:
    for i in range(n+1):
        f.write('{} {}\n'.format(t[i], y[i]))

# Plot the results
plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('y')
plt.show()