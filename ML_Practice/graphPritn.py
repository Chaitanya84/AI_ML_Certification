import matplotlib.pyplot as plt
import numpy as np
import csv

# Generate x range from 1 to 100
x = np.arange(1, 101)
y = 3*x

# Generate random points above and below the line
np.random.seed(42)  # for reproducible randomness
noise = np.random.randint(-30, 30, size=len(x))  # random offsets
random_points = y + noise

# Save red dot coordinates to CSV
with open("red_dot_coordinates.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["X", "Y"])  # Header
    for xi, yi in zip(x, random_points):
        writer.writerow([xi, yi])

print("CSV file 'red_dot_coordinates.csv' has been generated successfully!")

# Plot the line
plt.plot(x, y, label="Best Fit line", linewidth=2)

# Plot random points
plt.scatter(x, random_points, color="red", label="Real world sample")

# Label axes
plt.xlabel("Size")
plt.ylabel("Price")
plt.title("Linear Regression Line with Sample Points")

# Show legend and graph
plt.legend()
plt.show()
