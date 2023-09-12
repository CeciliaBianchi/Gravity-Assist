import numpy as np
import matplotlib.pyplot as plt

# Constants of the Planet
G = 6.67430e-11  # (m^3/kg/s^2)
planet_mass = 5.972e24  # Earth(kg)

# Constants of the SpaceCraft
spacecraft_mass = 1000  # (kg)
initial_x_velocity = 10000  # (m/s)
initial_y_velocity = 0  # (m/s)
initial_position = np.array([0, 6371000 + 100000])  # (m)

# Espace velocity
R = 63710000 + 100000
escape_velocity = np.sqrt(2 * G * planet_mass / R)

# Simulation Parameters
dt = 1  # Time stamp to one second, updating position and velocity of the spacecraft
total_time = 24 * 3600
num_steps = int(total_time / dt)  # Number of time steps

# Store positions and velocity
positions = np.zeros((num_steps, 2))
velocities = np.zeros((num_steps, 2))

# Initial Velocity
velocities[0] = np.array([initial_x_velocity, initial_y_velocity])
positions[0] = initial_position

# Simulation
for step in range(1, num_steps):
    # Calculate gravitational force acting on the spacecraft at its current position
    r = positions[step - 1]  # Current position
    r_norm = np.linalg.norm(r)  # Calculate the Euclidean norm

    # Check if r_norm is zero; if so, set the force to zero
    if r_norm == 0:
        F_gravity = np.array([0, 0])
    else:
        # Formula for gravitational force, -G because the force is attracting the spacecraft towards the planet
        # r_norm**3 -> inverse cube of the distance r_norm
        # * r -> direction of the force
        F_gravity = -G * (spacecraft_mass * planet_mass / r_norm**3) * r

    # Update velocity and position
    velocities[step] = velocities[step-1] + (F_gravity / spacecraft_mass) * dt
    positions[step] = positions[step-1] + velocities[step] * dt

    # Debugging print statements
    if step % 1000 == 0:
        print(
            f"Step {step}: Position = {positions[step]}, Velocity = {velocities[step]}")

# Visualize the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(positions[:, 0], positions[:, 1])
plt.title("Spacecraft Trajectory")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")

plt.subplot(1, 2, 2)
plt.plot(np.arange(0, total_time, dt), np.linalg.norm(velocities, axis=1))
plt.title("Spacecraft Velocity")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")

plt.tight_layout()
plt.show()
