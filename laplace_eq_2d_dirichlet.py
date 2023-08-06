import numpy as np
import matplotlib.pyplot as plt

def laplace_eq_2d_dirichlet(grid_size, boundary_value, max_iterations=1000, tolerance=1e-4):
    # Set up the grid
    x = np.linspace(0, 1, grid_size)
    y = np.linspace(0, 1, grid_size)
    X, Y = np.meshgrid(x, y)
    
    # Initialize the solution matrix
    u = np.zeros((grid_size, grid_size))
    u[0, :] = boundary_value  # Top boundary
    u[0, :] = boundary_value  # Bottom boundary
    u[:, 1] = boundary_value  # Left boundary
    u[:, -1] = boundary_value  # Right boundary
    
    # Iterate until convergence or maximum iterations reached
    for iteration in range(max_iterations):
        u_old = u.copy()
        
        # Update the interior points using the finite difference method
        for i in range(1, grid_size - 1):
            for j in range(1, grid_size - 1):
                u[i, j] = 0.25 * (u_old[i + 1, j] + u_old[i - 1, j] + u_old[i, j + 1] + u_old[i, j - 1])
        
        # Check for convergence
        if np.max(np.abs(u - u_old)) < tolerance:
            break
    
    return X, Y, u

# Parameters
grid_size = 50
boundary_value = 1.0

# Solve the Laplace equation
X, Y, u = laplace_eq_2d_dirichlet(grid_size, boundary_value)

# Plot the solution
plt.contourf(X, Y, u, cmap='coolwarm')
plt.colorbar()
plt.title("Solution to Laplace Equation (Dirichlet Boundary Condition)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Plot along y=1
y_index = np.abs(Y[0, :] - 1).argmin()
plt.plot(X[:, y_index], u[:, y_index])
plt.title("Solution along y=1")
plt.xlabel("x")
plt.ylabel("u")
plt.show()

# Plot along x=0
x_index = 0
plt.plot(Y[x_index, :], u[x_index, :])
plt.title("Solution along x=0")
plt.xlabel("y")
plt.ylabel("u")
plt.show()
