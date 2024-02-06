import matplotlib.pyplot as plt
import numpy as np

# Specify file path
file_path = 'output.dat'

# Read data from the file
data = np.loadtxt(file_path)
x_values, y_values = data[:, 0], data[:, 1]

# Plot the data
plt.stem(x_values, y_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.ylabel('x(n)')
plt.xlabel('n')
plt.grid(True)

plt.show()
