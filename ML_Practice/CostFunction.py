#This is and attempt to implement a simple cost function for linear regression in Python.
import matplotlib.pyplot as plt
import numpy as np
import csv

#reading the red dot coordinates from CSV file
x = []
y = []
with open("red_dot_coordinates.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))
x = np.array(x)
y = np.array(y)
# Initialize parameters
m = 0  # slope
b = 0  # y-intercept
learning_rate = 0.0001
iterations = 1000
n = len(x)  # number of data points
# Cost function
def compute_cost(x, y, m, b):
    total_cost = 0
    for i in range(n):
        total_cost += (y[i] - (m * x[i] + b)) ** 2
        #write error and squared error for all iterations to csv
        with open("errors.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            error = y[i] - (m * x[i] + b)
            squared_error = error ** 2
            writer.writerow([i, error, squared_error])
            
        #plot the error lines        
        #plt.plot([x[i], x[i]], [y[i], m * x[i] + b], color="green", linestyle="--", linewidth=0.5)
    return total_cost / (2 * n)
# Gradient descent
for _ in range(iterations):
    m_gradient = 0
    b_gradient = 0
    for i in range(n):
        m_gradient += -x[i] * (y[i] - (m * x[i] + b))
        b_gradient += -(y[i] - (m * x[i] + b))
    m -= (learning_rate * m_gradient) / n
    b -= (learning_rate * b_gradient) / n
    if _ % 100 == 0:
        cost = compute_cost(x, y, m, b)
        print(f"Iteration {_}: Cost {cost}, m {m}, b {b}")

# Final parameters
print(f"Final parameters: m = {m}, b = {b}")
#plot the error lines for final iteration
for i in range(n):
    plt.plot([x[i], x[i]], [y[i], m * x[i] + b], color="green", linestyle="--", linewidth=0.5)  

# Plotting the results
plt.scatter(x, y, color="red", label="Real world sample")
plt.plot(x, m * x + b, color="blue", label="Fitted line")
plt.xlabel("Size")
plt.ylabel("Price")
plt.title("Linear Regression Fit using Gradient Descent")
plt.legend()
plt.show() 
