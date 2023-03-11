import matplotlib.pyplot as plt
import numpy as np


def plot(x, y, x_derivative, y_derivative, x_point, y_point, x_tangent, y_tangent, title, x_label, y_label):
    plt.style.use('dark_background')
    plt.plot(x, y, 'fuchsia', label='f(x) = x^2', linewidth=2)
    plt.plot(x_derivative, y_derivative, 'lime', label='f\'(x) = 2x', linewidth=2)
    plt.plot(x_point, y_point, marker='o', c='red', label='point of interest')
    plt.plot(x_tangent, y_tangent, linestyle='dashed', c='snow', label='tangent line', linewidth=1)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.legend(loc='upper left')
    plt.show()


# create f(x) data points
x_data = np.linspace(-100, 100, num=1000)
y_data = x_data**2

# create f'(x) data points
x_derivative_data = np.linspace(-100, 100, num=1000)
y_derivative_data = 2*x_data

# create tangent line data points
# equation of tangent line: y = m(x-x1) + y1
x1 = 50
y1 = x1**2
x_tangent_data = np.linspace(30, 70, num=1000)
y_tangent_data = (2*x1)*(x_tangent_data - x1) + y1

# plot
plot(x_data, y_data, x_derivative_data, y_derivative_data, x1, y1, x_tangent_data, y_tangent_data, 'Derivatives', 'x', 'y')

