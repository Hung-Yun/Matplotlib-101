
"""

Use annotation to point the most important part of your graph!

"""

import matplotlib.pyplot as plt
import numpy as np

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2) # We can use lw instead of linewidth for brevity

plt.annotate('local max', # The information of the annotation
             xy=(2, 1), xytext=(2.5,1.4), # The position of the arrow and the text
             # As for arrowprops, the information should be stored in a dictionary
             arrowprops=dict(facecolor='black', shrink=0.1, width=0.5, headwidth=10)
             )

plt.ylim(-1.2, 1.7) # If we want to limit the y axis, use ylim. plt.axis would affect the x axis as well
plt.show() # Annotation_with_text
