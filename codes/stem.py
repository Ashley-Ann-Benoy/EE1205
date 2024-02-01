import numpy as np
import matplotlib.pyplot as plt

# Function to generate the sequence x(n)
def x_n(n):
    return (5 * n + 1) * (n >= 0)

# Generate values for n
n_values = np.arange(0, 10, 1)

# Generate the sequence x(n)
x_values = x_n(n_values)

# Create a stem plot with a grid
plt.stem(n_values, x_values, basefmt='b-', linefmt='r-', markerfmt='ro')

# Add a grid to the plot
plt.grid(True)

# Set plot labels and title
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem Plot of x(n) = (5n + 1)u(n)')

# Show the plot
plt.show()

