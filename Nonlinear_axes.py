
"""

Specify the y scale to linear, log, symlog mode

"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale

# Fixing random state for reproducibility.
# If we use np.random.seed(), the outcome of random value would be fixed
np.random.seed(19680801)

# make up some data in the interval [0,1]
y = np.random.normal(size=2000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure(1,figsize=(10,3))

# linear
plt.subplot(131)
plt.plot(x, y)
plt.yscale('linear') # We only need to specify the scale of y by plt.yscale
plt.title('linear')
plt.grid(True)


# log
plt.subplot(132)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(133)
plt.plot(x, y-y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

plt.show()
