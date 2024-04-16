import cv2 as cv
import numpy as np
import sys

colors = ['red', 'green', 'blue']

img = cv.imread(sys.argv[1])
width = img.shape[1]
height = img.shape[0]
pixels = width * height
img = np.reshape(img, pixels * 3)

bit_planes = np.array([0, 1, 2, 7], dtype=np.uint8) # choose bit-planes
zeros = np.zeros(pixels, dtype=np.uint8)

for plane in bit_planes:
    for i in range(3):
        bit_slicing = [zeros, zeros]
        extraction_plane = ((img[i::3] >> plane) & 1) * 255
        bit_slicing.insert(i, extraction_plane)
        bit_slicing = np.array(bit_slicing)
        bit_slicing = np.stack(bit_slicing[::-1]).ravel('F')
        bit_plane_map = np.reshape(bit_slicing, (height, width, 3))
        cv.imwrite(f'{colors[i]}-{plane}.png', bit_plane_map)



