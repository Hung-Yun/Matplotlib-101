
"""

Matplotlib allows you provide such an object with the data keyword argument.
If provided, then you may generate plots with the strings corresponding to these variables.

"""

import matplotlib.pyplot as plt
import numpy as np

data = {'a': np.arange(50),
        'c': np.random.randint(0,50,50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', # Scatter plot, the first argument is x axis, the second is y
            c='c', # It means the color of each dot could be assigned by an array
            s='d', # It means the size of each dot could also be assigned by an array
            data=data) # We must assign the data to the dictionary

# Change the label of each axis
plt.xlabel('entry a')
plt.ylabel('entry b')

plt.show() # Plot_with_keyword_string
