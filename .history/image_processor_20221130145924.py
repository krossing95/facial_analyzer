# # from deepface import DeepFace
# import imutils
# import cv2
# # from urllib.request import urlopen
# # import numpy as np

# url = 'https://png.pngtree.com/png-vector/20210303/ourmid/pngtree-mobile-phone-png-smartphone-camera-mockup-png-image_3009179.jpg'
# read = imutils.url_to_image(url, readFlag=cv2.IMREAD_COLOR)
# print(read)
import requests
import numpy as np
from io import BytesIO
from PIL import Image


def url_to_img(url, save_as=''):
    img = Image.open(url)
    if save_as:
        img.save(save_as)
        print(np.array(img))
    return np.array(img)


url_to_img('https://png.pngtree.com/png-vector/20210303/ourmid/pngtree-mobile-phone-png-smartphone-camera-mockup-png-image_3009179.jpg')
