# Gravitational Simulation

This Python script simulates the motion of a spacecraft in the gravitational field of a planet using numerical methods. The simulation calculates the trajectory and velocity of the spacecraft over time, taking into account the gravitational force acting on it.

## Prerequisites

Before running the simulation, make sure you have the following installed:

- **Python:** You can download it from [python.org](https://www.python.org/downloads/).

- **Required Python packages:** NumPy and Matplotlib. Install them using the following command:

    ```bash
    pip install numpy matplotlib
    ```

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/gravitational-simulation.git
    cd gravitational-simulation
    ```

2. **Run the simulation:**

    ```bash
    python gravitational_simulation.py
    ```

3. **Explore the results:**

    The script generates a visual representation of the spacecraft's trajectory and velocity over time using Matplotlib.

## Simulation Parameters

The simulation includes constants for the planet and spacecraft, such as gravitational constant, masses, initial velocities, and initial position. These parameters can be modified in the script to observe the impact on the simulation.

## Visualization

The results are visualized using Matplotlib, creating two plots:

1. **Spacecraft Trajectory:**
   - X-axis represents the X position of the spacecraft.
   - Y-axis represents the Y position of the spacecraft.

2. **Spacecraft Velocity:**
   - X-axis represents time in seconds.
   - Y-axis represents the magnitude of the spacecraft's velocity.

## Customization

Feel free to modify the script to experiment with different initial conditions, time steps, or simulation durations. This can provide insights into how changing parameters affects the spacecraft's motion in a gravitational field.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This simulation is a basic example and might not represent real-world scenarios accurately. It is meant for educational purposes and understanding the fundamentals of gravitational motion.
