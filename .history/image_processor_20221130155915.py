from deepface import DeepFace
import urllib.request
import cv2 as cv2
import numpy as np
import os
import datetime

url = '''https://ca-times.brightspotcdn.com/dims4/default/83de13e/2147483647/strip/true/crop/2000x2706+0+0/resize/1200x1624!/quality/80/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2Fff%2F2c%2Fdedf568e4af087cab5f0a5c76f32%2Fla-ca-bk-a-promised-land-barack-obama-183.JPG'''
url2 = '''https://cdn.britannica.com/43/172743-138-545C299D/overview-Barack-Obama.jpg'''


class imgList:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename


img_list = []
img_list.append(imgList(url, 'obama1.png'))
img_list.append(imgList(url2, 'obama2.png'))

files = []


def getImage(url, filename):
    url_response = urllib.request.urlopen(url)
    img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    if (os.path.isdir(filename)):
        os.remove(filename)
    return cv2.imwrite(filename, img)


def callImage():
    for i in img_list:
        files.append(i.filename)
    return files


for i in img_list:
    getImage(i.url, i.filename)
print(callImage())
