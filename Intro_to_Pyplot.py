
"""
matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB.
Each pyplot function makes some change to a figure.
For example, creates a figure, creates a plotting area in a figure,
plots some lines in a plotting area, decorates the plot with labels, etc.
"""

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show() # Intro_to_Pyplot_1

"""
Why is the x-axis ranges from 0-3 and the y-axis from 1-4?
If you provide a single list or array to the matplotlib.pyplot.plot command,
matplotlib assumes it is a sequence of y values, and automatically generates the x values for you.
Since python ranges start with 0, the default x vector has the same length as y but starts with 0.
Hence the x data are [0,1,2,3].
"""

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show() # Intro_to_Pyplot_2

"""
The first list is the vector of x axis, the second list is for y.
"""
