
"""
Formatting the style of Pyplot.
For each pair of x and y arguments, there is an optional third argument.
It is the format string that indicates the color and line type of the plot.
matplotlib.pyplot.axis command takes a list of [xmin, xmax, ymin, ymax].
"""

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') # r is red, o is circle
plt.axis([0, 6, 0, 20])
plt.show() # Style_of_Pyplot_1


import numpy as np
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show() # Style_of_Pyplot_2
