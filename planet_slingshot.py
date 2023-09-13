import numpy as np
import matplotlib.pyplot as plt

# Constants of the SpaceCraft
spacecraft_mass = 1000  # (kg)
initial_x_velocity = 8000  # (m/s)
initial_y_velocity = 0  # (m/s)
initial_position = np.array([0, 6371000 + 100000])  # (m)

# Constants of the Planet
G = 6.67430e-11  # (m^3/kg/s^2)
planet_mass = 5.972e24  # Earth(kg)

# Multiple planet data
planet_data = [
    {"name": "Earth", "mass": 5.972e24, "radius": 6371000 + 100000},
    {"name": "Mars", "mass": 6.39e23, "radius": 3.37e6}
]

# Simulation Parameters
G = 6.67430e-11
dt = 1  # Time stamp
total_time = 24 * 3600
num_steps = int(total_time / dt)  # Number of time steps

# Store positions and velocity
positions = np.zeros((num_steps, 2))
velocities = np.zeros((num_steps, 2))

# Initial Velocity
velocities[0] = np.array([initial_x_velocity, initial_y_velocity])
positions[0] = initial_position

# Flag spacecraft has enter Mars' sphere of influence
mars_soi_entered = False

# Simulation
for step in range(1, num_steps):
    # Calculate gravitational force
    total_force = np.array([0.0, 0.0])  # Initialize total force to zero

    for planet in planet_data:
        planet_mass = planet["mass"]
        planet_radius = planet["radius"]
        planet_position = np.array([0, 0])
        planet_position[1] = planet_radius

        r = planet_position - positions[step - 1]  # Current position
        r_norm = np.linalg.norm(r)  # Calculate the Euclidean norm

        # Check if r_norm is zero; if so, set the force to zero
        if r_norm == 0:
            F_gravity = np.array([0, 0])
        else:
            F_gravity = -G * (spacecraft_mass * planet_mass / r_norm**3) * r
        total_force += F_gravity

    print(f"Step {step}: Total Force = {total_force}")

    # Update velocity and position
    velocities[step] = velocities[step-1] + \
        (total_force / spacecraft_mass) * dt
    positions[step] = positions[step-1] + velocities[step] * dt

    # Check if spacecraft enters Mars' sphere of influence
    if not mars_soi_entered and np.linalg.norm(positions[step] - planet_data[1]["radius"]) < planet_data[1]["radius"]:
        mars_soi_entered = True
        # Adjust the spacecraft velocity for gravity assist from Mars
        v_infinity = np.linalg.norm(velocities[step] - velocities[step - 1])
        v_escape = np.sqrt(
            2 * G * planet_data[1]["mass"] / planet_data[1]["radius"])
        delta_v = v_escape - v_infinity
        velocities[step] += delta_v

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
plt.plot(np.arange(0, total_time, dt), -np.linalg.norm(velocities, axis=1))
plt.title("Spacecraft Velocity")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")

plt.tight_layout()
plt.show()
