import matplotlib.pyplot as plt
import numpy as np

# Define the differential equation to solve: x_dot = cos(πt)
def f(t, x):
    return np.cos(np.pi * t)

# Define the initial conditions
t0 = 0
x0 = 0

# Define the step size and number of steps
h = 0.01

n = int((10 - t0) / h)  # Calculate the number of steps based on the interval [0, 10]

# Initialize arrays for t and x values
t = np.zeros(n+1)
x = np.zeros(n+1)

# Set initial values
t[0] = t0
x[0] = x0

# Solve the ODE using the Euler method
for i in range(n):
    t[i+1] = t[i] + h
    x[i+1] = x[i] + h * f(t[i], x[i])

# Plot the results
plt.plot(t, x)
plt.xlabel('t')
plt.ylabel('x')
plt.title('Numerical Solution of x_dot = cos(πt)')
plt.show()

