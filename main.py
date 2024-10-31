from sympy import symbols
import matplotlib.pyplot as plt
import numpy as np

# Define symbols
t = symbols('t')

# Define constants for initial velocity and acceleration
v = 5       # Initial velocity in m/s
a = 2       # Acceleration in m/s^2

# Define the distance function
d_t = v * t + (1/2) * a * t**2

# Convert the symbolic expression to a numerical function using lambdify
from sympy import lambdify
distance_function = lambdify(t, d_t, 'numpy')

# Generate time values
time_values = np.linspace(0, 10, 100)
distance_values = distance_function(time_values)

# Define the single point to display
single_time = 3  # example time
single_distance = distance_function(single_time)

# Plot the distance-time graph
plt.plot(time_values, distance_values, label="Distance over time")
plt.scatter(single_time, single_distance, color='red', marker='o', s=50, label=f"Point at t={single_time}")

# Labels and legend
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.title("Distance-Time Graph with Single Point")
plt.legend()

# Show plot
plt.show()