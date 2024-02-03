import matplotlib.pyplot as plt
import numpy as np

def read_points_from_file(file_path):
    data = np.loadtxt('output.dat')
    x_values = data[:, 0]
    y_values = data[:, 1]
    return x_values, y_values

def plot_points(x_values, y_values):
    plt.stem(x_values, y_values, linefmt='b-', markerfmt='bo', basefmt='r-')
    plt.ylabel('x(n)')
    plt.xlabel('n')
    plt.grid(True)
    plt.title('Stem Plot of x(n)=(5n+1)u(n)')
    plt.show()

def main():
    file_path = 'your_file.txt'  # Replace with the path to your text file
    x_values, y_values = read_points_from_file(file_path)
    plot_points(x_values, y_values)

if __name__ == "__main__":
    main()
