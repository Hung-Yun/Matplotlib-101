
"""

Introducing how to put legend into your graph

"""

import matplotlib.pyplot as plt

# Create x
import numpy as np
x = np.linspace(0, 2, 100)

plt.plot(x, x, x, x**2, x, x**3)
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Plot")

"""

The first argument is the labels of each data.
loc means the location of this legend, it follows a table which could be found below.
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html
For example, loc=10 means the legend would be placed at the center.
frameon=False means that I turn off the frame of my legend
There are also other fancy tools regarding to legend.
Please also check on the website above to find more customization attributes!

"""
plt.legend(('linear', 'quadratic', 'cubic'), loc=10, frameon=False)

plt.show()
