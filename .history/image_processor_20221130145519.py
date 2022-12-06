# from deepface import DeepFace
import imutils
import cv2
# from urllib.request import urlopen
# import numpy as np

url = 'https://png.pngtree.com/png-vector/20210303/ourmid/pngtree-mobile-phone-png-smartphone-camera-mockup-png-image_3009179.jpg'
read = imutils.url_to_image(url, readFlag=cv2.IMREAD_COLOR)
print(read)
