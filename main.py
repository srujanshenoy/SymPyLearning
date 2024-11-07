from sympy import symbols, plot

# Define the time symbol and constants
t = symbols('t')
v = 5       # Initial velocity in m/s
a = 2       # Acceleration in m/s^2

# Define the distance function
d_t = v * t + (1/2) * a * t**2

# Define the time point to highlight, say t = 3
single_time = 3
single_distance = d_t.subs(t, single_time)  # Calculate distance at t = 3

# Plot the distance-time function and add a "point" as a narrow vertical line at t = 3
p = plot(d_t, (t, 0, 10), show=False, label="Distance over time")
p.extend(plot(single_distance, (t, single_time - 0.01, single_time + 0.01), 
              line_color='red', marker='o', markersize=10, show=False, label=f"Point at t={single_time}"))

# Display the plot
p.show()
