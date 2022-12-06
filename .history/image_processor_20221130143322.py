from deepface import DeepFace
import cv2
from urllib.request import urlopen
import numpy as np

url = 'http://answers.opencv.org/upfiles/logo_2.png'
url_resp = urlopen(url)
img_array = np.array(bytearray(url_resp.read()), dtype=np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
cv2.waitKey()