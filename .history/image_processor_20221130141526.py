from deepface import DeepFace
import cv2
from urllib.request import urlopen
import numpy as np


def url_to_image(url, readFlag=cv2.IMREAD_COLOR):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, readFlag)

    # return the image
    print(image)
    return image


url_to_image('http://answers.opencv.org/upfiles/logo_2.png')
