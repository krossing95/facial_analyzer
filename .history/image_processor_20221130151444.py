# # from deepface import DeepFace
import urllib.request
import cv2 as cv2
import numpy as np

url = "https://media.geeksforgeeks.org/wp-content/uploads/20211003151646/geeks14.png"
url_response = urllib.request.urlopen(url)
img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
img = cv2.imdecode(img_array, 0)
img1 = cv2.imwrite("result.jpg", img)
print(img1)
# cv2.imshow('URL Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
