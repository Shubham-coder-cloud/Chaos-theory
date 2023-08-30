import numpy as np
import matplotlib.pyplot as plt

# Parameters
L1 = 1.0  # Length of the first pendulum arm
L2 = 0.8  # Length of the second pendulum arm

# Initial conditions
theta1 = np.pi / 2
theta2 = np.pi / 2
omega1 = 0.0
omega2 = 0.0
dt = 0.01
num_steps = 10000

# Initialize arrays to store positions of the second bob
x2_path = []
y2_path = []

for _ in range(num_steps):
    alpha = (L1 / L2) * (1 + (L2 / L1) * np.cos(theta1 - theta2))
    
    omega1 += (-9.81 / L1 * np.sin(theta1) - alpha * omega2**2 * np.sin(theta1 - theta2)) * dt
    omega2 += (-9.81 / L2 * np.sin(theta2) + alpha * omega1**2 * np.sin(theta1 - theta2)) * dt
    
    theta1 += omega1 * dt
    theta2 += omega2 * dt
    
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)
    
    x2_path.append(x2)
    y2_path.append(y2)

# Plotting the fractal path of the second bob in red
plt.plot(x2_path, y2_path, color='red')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('Fractal Path of Second Bob in a Two-Joint Pendulum')
plt.show()
