
"""

Put texts into the figure using plt.text.
The first two arguments are the position of the x,y coordinate.
The string is the information.
There will be a full introduction of text in the future!

"""

import matplotlib.pyplot as plt
import numpy as np

# The data 
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# Create a figure (This step could be ignored if only one figure needed)
plt.figure(1)

# Histogram, x, bins, facecolor, alpha, density
# If density is True, the first element of the return tuple will be the counts normalized to form a probability density.
plt.hist(x, bins=100, density = True , facecolor='g', alpha=0.75)

# Change the label of each axis
plt.xlabel('Smarts')
plt.ylabel('Probability')

# Change the title
plt.title('Histogram of IQ')

# Put texts into the figure using plt.text.
plt.text(60, .025, '$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True, alpha = 0.5)

plt.show()

