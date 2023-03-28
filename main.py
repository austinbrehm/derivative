import matplotlib.pyplot as plt
import numpy as np


def plot(x, y, x_derivative, y_derivative, x_point, y_point, x_tangent, y_tangent, title, x_label, y_label):
    plt.style.use('dark_background')
    plt.plot(x, y, 'fuchsia', label='f(x) = x^2', linewidth=2)
    plt.plot(x_derivative, y_derivative, 'lime', label='f\'(x) = 2x', linewidth=2)
    plt.plot(x_point, y_point, marker='o', c='red', label='point of interest')
    plt.plot(x_tangent, y_tangent, linestyle='dashed', c='pink', label='tangent line', linewidth=1)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.legend(loc='upper left')
    plt.show()


# create data points for f(x) and f'(x)
x_data = np.linspace(-100, 100, num=1000)
y_data = x_data**2
y_derivative_data = 2*x_data

# create point of interest: (x0, y0)
x0 = 50
y0 = x0**2

# create tangent line: y = m(x-x0) + y0
x_tangent_data = np.linspace(30, 70, num=1000)
y_tangent_data = (2*x0)*(x_tangent_data - x0) + y0

# plot
plot(x_data, y_data, x_data, y_derivative_data, x0, y0, x_tangent_data, y_tangent_data, 'Derivatives', 'x', 'y')

