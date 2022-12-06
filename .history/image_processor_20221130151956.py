# # from deepface import DeepFace
import urllib.request
import cv2 as cv2
import numpy as np
import os

url = "https://media.sproutsocial.com/uploads/2017/02/10x-featured-social-media-image-size.png"
url_response = urllib.request.urlopen(url)
img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
os.remove('result.jpg')
img1 = cv2.imwrite("result.jpg", img)
