import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.randn(2, 1000)

plt.figure(1,figsize=(6,6))

plt.subplot(221)
plt.hist(data[0])
plt.title("Histogram")

plt.subplot(222)
plt.scatter(data[0],data[1])
plt.title("Scatter")

plt.subplot(223)
plt.plot(data[0],data[1])
plt.title("Line")

plt.subplot(224)
plt.hist2d(data[0],data[1],bins=30)
plt.title("Histogram 2D")

plt.show()
