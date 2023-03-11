import matplotlib.pyplot as plt
import numpy as np


def plot(x, y, x_derivative, y_derivative, title, x_label, y_label):
    plt.style.use('dark_background')
    plt.plot(x, y, 'fuchsia', label='f(x) = x**2', linewidth=1)
    plt.plot(x_derivative, y_derivative, 'lime', label='f\'(x) = 2*x', linewidth=1)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.legend(loc='upper left')
    plt.show()


# create data points
x_data = np.linspace(-100, 100, num=1000)
y_data = x_data**2

# create derivative data points
x_derivative_data = np.linspace(-100, 100, num=1000)
y_derivative_data = 2*x_data

# plot
plot(x_data, y_data, x_derivative_data, y_derivative_data, 'Derivatives', 'x', 'y')

