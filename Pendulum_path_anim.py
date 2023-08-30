import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
L1 = 1.0  # Length of the first pendulum arm
L2 = 0.8  # Length of the second pendulum arm
g = 9.81  # Acceleration due to gravity

# Initial conditions
theta1 = np.pi / 2
theta2 = np.pi / 2
omega1 = 0.0
omega2 = 0.0
dt = 0.01
num_steps = 1000

# Animation initialization function
def init():
    line.set_data([], [])
    return line,

# Animation update function
def animate(i):
    global theta1, theta2, omega1, omega2

    alpha = (L1 / L2) * (1 + (L2 / L1) * np.cos(theta1 - theta2))
    
    omega1 += (-g / L1 * np.sin(theta1) - alpha * omega2**2 * np.sin(theta1 - theta2)) * dt
    omega2 += (-g / L2 * np.sin(theta2) + alpha * omega1**2 * np.sin(theta1 - theta2)) * dt
    
    theta1 += omega1 * dt
    theta2 += omega2 * dt
    
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)
    
    line.set_data([0, x1, x2], [0, y1, y2])
    ax.set_xlim(-(L1 + L2), L1 + L2)
    ax.set_ylim(-(L1 + L2), L1 + L2)
    ax.set_title(f'Time step: {i}')
    return line,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-(L1 + L2), L1 + L2)
ax.set_ylim(-(L1 + L2), L1 + L2)
line, = ax.plot([], [], 'o-', color='blue')

# Create the animation
ani = FuncAnimation(fig, animate, frames=num_steps, init_func=init, blit=True)

plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('Animated Motion of Two-Joint Pendulum')
plt.show()
