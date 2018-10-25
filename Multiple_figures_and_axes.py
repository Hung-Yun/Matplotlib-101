
"""

Multiple figures and axes

"""

import matplotlib.pyplot as plt
import numpy as np

# Define a wierd function to be used in subplot 1
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1,figsize=(7,7))
plt.subplot(211) # The subplots are arranged as 2x1 configuration.
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.figure(2) # Now we create a second figure, Figure_2
plt.plot([4, 5, 6])

plt.figure(1) # We can trace back to the first figure
plt.subplot(212) # and specify the subplot we intend to manage
plt.title("This is the title") # Create a title for the subplot

plt.show() # Multiple_figures_and_axes_1, Multiple_figures_and_axes_2
