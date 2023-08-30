import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lorenz system parameters
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Time parameters
dt = 0.01
num_steps = 10000

# Range of initial conditions for x
initial_conditions_x = np.linspace(0.1, 1.0, num=10)

# Fixed initial conditions for y and z
y0, z0 = 0.0, 0.0

# Create a 3D plot for each initial condition of x
fig = plt.figure(figsize=(12, 10))

for x0 in initial_conditions_x:
    x, y, z = x0, y0, z0
    x_vals = []
    y_vals = []
    z_vals = []

    for i in range(num_steps + 1):
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        x += dx * dt
        y += dy * dt
        z += dz * dt
        x_vals.append(x)
        y_vals.append(y)
        z_vals.append(z)

    ax = fig.add_subplot(3, 4, initial_conditions_x.tolist().index(x0) + 1, projection='3d')
    ax.plot(x_vals, y_vals, z_vals, linewidth=0.5)
    ax.set_title(f'Initial x = {x0}, y = {y0}, z = {z0}')

plt.tight_layout()
plt.show()