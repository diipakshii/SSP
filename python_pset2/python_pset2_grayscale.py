# grayscale image
# Grayscale
# 06/16/22
# Dipakshi Pal

import matplotlib.pyplot as plt
from astropy.io import fits 

# beach_portrait.png is an RGB image, so image is a 3D array with 3 values at each pixel location
# the slice is to remove an unnecessary alpha channel, if present
# save the data in gray_image as a grayscale image to a file called beach_portrait_gray.png

image = plt.imread("beach_portrait.png")[:, :, :3]

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        rgb = image[i,j]
        if rgb[0] != rgb[1] != rgb[2]:
            image[i,j] = (rgb[0] + rgb[1] + rgb[2])/3      

plt.imshow(image)

plt.gray()
plt.show()
plt.imsave("beach_portrait_gray.png", image)