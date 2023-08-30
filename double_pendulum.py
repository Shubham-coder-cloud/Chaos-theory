import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
L1 = 1.0  # Length of the first pendulum arm
L2 = 0.8  # Length of the second pendulum arm
m1 = 1.0  # Mass of the first pendulum bob
m2 = 0.8  # Mass of the second pendulum bob
g = 9.81  # Acceleration due to gravity

# Initial conditions
theta1_0 = np.pi / 2  # Initial angle of the first pendulum
theta2_0 = np.pi / 2  # Initial angle of the second pendulum
omega1_0 = 0.0       # Initial angular velocity of the first pendulum
omega2_0 = 0.0       # Initial angular velocity of the second pendulum

# Time parameters
dt = 0.01   # Time step
t_max = 20  # Maximum simulation time

# Function to update pendulum angles and velocities
def update_pendulum(state, dt):
    theta1, theta2, omega1, omega2 = state
    
    # Angular Acceleration of the First Pendulum
    alpha1_num = -g * (2 * m1 + m2) * np.sin(theta1) - m2 * g * np.sin(theta1 - 2 * theta2) - 2 * np.sin(theta1 - theta2) * m2 * (omega2**2 * L2 + omega1**2 * L1 * np.cos(theta1 - theta2))
    alpha1_den = L1 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2))
    alpha1 = alpha1_num / alpha1_den
    
    # Angular Acceleration of the Second Pendulum
    alpha2_num = 2 * np.sin(theta1 - theta2) * (omega1**2 * L1 * (m1 + m2) + g * (m1 + m2) * np.cos(theta1) + omega2**2 * L2 * m2 * np.cos(theta1 - theta2))
    alpha2_den = L2 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2))
    alpha2 = alpha2_num / alpha2_den
    
    omega1_new = omega1 + alpha1 * dt
    omega2_new = omega2 + alpha2 * dt
    theta1_new = theta1 + omega1_new * dt
    theta2_new = theta2 + omega2_new * dt
    
    return theta1_new, theta2_new, omega1_new, omega2_new

# Initialize the pendulum state
state = (theta1_0, theta2_0, omega1_0, omega2_0)

# Initialize lists to store pendulum positions
theta1_vals = []
theta2_vals = []

# Simulate the pendulum motion
for t in np.arange(0, t_max, dt):
    theta1_vals.append(state[0])
    theta2_vals.append(state[1])
    state = update_pendulum(state, dt)

# Convert polar coordinates to Cartesian coordinates
x1 = L1 * np.sin(theta1_vals)
y1 = -L1 * np.cos(theta1_vals)
x2 = x1 + L2 * np.sin(theta2_vals)
y2 = y1 - L2 * np.cos(theta2_vals)

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-(L1 + L2), L1 + L2)
ax.set_ylim(-(L1 + L2), L1 + L2)
line, = ax.plot([], [], 'o-')

def init():
    line.set_data([], [])
    return line,

def animate(i):
    line.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
    return line,

ani = FuncAnimation(fig, animate, frames=len(x1), init_func=init, blit=True)

plt.show()