
"""

Import an image and find the information of this image

"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

"""
In the beginning, the result raised ValueError:
Only know how to handle extensions: ['png'];
with Pillow installed matplotlib can handle more images
Therefore, I installed pillow (pip3 install pillow in the command line)
then it worked
"""

img = mpimg.imread('einstein.jpg')
print(img.shape)
# Let's print the data of this image as an array
# We can find that it is an 3d array, each pixel contains 3 element.

plt.figure(1,figsize=(8,5))
plt.subplot(221)
plt.imshow(img)
plt.title("A")
plt.subplot(222)
lum_img = img[:, :, 0]
plt.imshow(lum_img)
plt.title("B")
plt.subplot(223)
plt.imshow(lum_img, cmap="hot")
plt.colorbar()
plt.title("C")
plt.subplot(224)
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')
plt.title("D")
plt.show()
