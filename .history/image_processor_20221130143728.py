from deepface import DeepFace
import cv2
from urllib.request import urlopen
import numpy as np

url = 'https://png.pngtree.com/png-vector/20210303/ourmid/pngtree-mobile-phone-png-smartphone-camera-mockup-png-image_3009179.jpg'
url_resp = urlopen(url)
print(url_resp)
# img_array = np.array(bytearray(url_resp.read()), dtype=np.uint8)
# img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)
# cv2.imshow('image', img)
# cv2.waitKey()
