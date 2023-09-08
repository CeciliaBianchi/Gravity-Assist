import numpy as np
# Matplotlib is used for visualization
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon

# Constants of the Planet
G = 6.67430e-11  # (m^3/kg/s^2)
planet_mass = 5.972e24  # Earth(kg)

# Constants of the SpaceCraft
spacecraft_mass = 1000  # (kg)
initial_velocity = 10000  # (m/s)
initial_position = np.array([0, 6371000 + 100000])  # (m)

# Simulation Parameters
dt = 1  # Time stamp to one second, updating position and velocity of the spacecraft
total_time = 24 * 3600
num_steps = int(total_time / dt)  # Number of time steps

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_facecolor('black')

# Visualization of the planet
planet_x = 0
planet_y = 0
planet_radius = 6.371e6  # Earth's radius in meters
planet_circle = Circle((planet_x, planet_y), planet_radius, color='blue')
ax.add_patch(planet_circle)

# Store positions and velocity
positions = np.zeros((num_steps, 2))
velocities = np.zeros((num_steps, 2))

# Simulation
for step in range(num_steps):
    # Calculate gravitational force acting on the spacecraft at its current position
    # r means position of an object relative to a reference point.
    r = positions[step]  # Current position
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

    # Visualization of the spacecraft as a triangle (you can adjust its size and appearance)
    spacecraft_x, spacecraft_y = positions[step]
    spacecraft_triangle = Polygon([[spacecraft_x, spacecraft_y + 1e4],
                                   [spacecraft_x + 1e4, spacecraft_y - 1e4],
                                   [spacecraft_x - 1e4, spacecraft_y - 1e4]],
                                  closed=True,
                                  facecolor='red')
    ax.add_patch(spacecraft_triangle)

# Set axis limits for the plot
ax.set_xlim(-2e6, 2e6)
ax.set_ylim(-2e6, 2e6)

# Results
plt.title("Gravity Assist Simulation")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")

plt.show()
