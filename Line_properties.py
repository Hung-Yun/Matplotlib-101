
"""

matplotlib.pyplot.setp command.

"""

import matplotlib.pyplot as plt

import numpy as np
t = np.arange(-20,20)

# Create a figure and specify its size
plt.figure(figsize = (6,3))
plt.suptitle("Line Properties")

# Create 2 subplots and identify each subplot by using sublpot(121) and sublpot(122)
plt.subplot(121)
lines = plt.plot(t, t**2, t, -t+30) # We can set plt.plot into a variable
plt.setp(lines, linewidth = 0.5, color = "r") # Use plt.setp to specify the linewidth and color of the line

plt.subplot(122)
line1, line2 = plt.plot(t, t**2, t, -t+30) # If we set plt.plot into two variables (since we have two lines in a plot)

# We can set the style of each line, respectively
plt.setp(line1, linewidth = 3.0, color = "g") 
plt.setp(line2, linewidth = 1.0, color = "black")

plt.show() # Line_properties
