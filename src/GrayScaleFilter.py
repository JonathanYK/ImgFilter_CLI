import imageio as iio
import numpy as np


def rgb2gray():

    pic = iio.imread('input.jpg')
    gray_filter = lambda rgb: np.dot(rgb[..., :3], [0.299, 0.587, 0.114])
    gray_scale_img = gray_filter(pic).astype(np.uint8)

    gray_scale_img = gray_scale_img.astype(np.uint8)
    iio.imwrite("grayscale.png", gray_scale_img)

rgb2gray()