import matplotlib.pyplot as plt
import numpy as np


def plot(x, y, title, x_label, y_label):
    plt.style.use('dark_background')
    plt.plot(x, y, 'fuchsia', linewidth=1)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.show()


# create data points
x_data = np.linspace(-100, 100, num=1000)
y_data = x_data**2

# plot
plot(x_data, y_data, 'f(x) = x**2', 'x', 'y')

