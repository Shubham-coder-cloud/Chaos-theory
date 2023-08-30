import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

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

# Create the figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Set the limits and labels for the plot
ax.set_xlim(-25, 25)
ax.set_ylim(-35, 35)
ax.set_zlim(5, 55)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Initialize an empty line
line, = ax.plot([], [], [], linewidth=0.5)

# Animation initialization function
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

# Animation update function
def animate(i):
    x0 = initial_conditions_x[i]
    x, y, z = x0, y0, z0
    x_vals = []
    y_vals = []
    z_vals = []

    for _ in range(num_steps + 1):
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        x += dx * dt
        y += dy * dt
        z += dz * dt
        x_vals.append(x)
        y_vals.append(y)
        z_vals.append(z)

    line.set_data(x_vals, y_vals)
    line.set_3d_properties(z_vals)
        
    return line,

# Create the animation
ani = FuncAnimation(fig, animate, init_func=init, frames=len(initial_conditions_x), interval=1000, blit=True)

plt.tight_layout()
plt.show()  