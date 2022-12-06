from deepface import DeepFace
import urllib.request
import cv2 as cv2
import numpy as np
import os

url = '''https://cdn.britannica.com/05/236505-050-17B6E34A/Elon-Musk-2022.jpg'''
url2 = '''https://cdn.britannica.com/45/223045-050-A6453D5D/Telsa-CEO-Elon-Musk-2014.jpg'''
image_source = './source/'


class imgList:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename


img_list = []
img_list.append(imgList(url, 'obama1.png'))
img_list.append(imgList(url2, 'obama2.png'))

files = []


def createImage(url, filename):
    url_response = urllib.request.urlopen(url)
    img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    file = "{}{}".format(image_source, filename)
    if (os.path.isdir(file)):
        os.remove(file)
    return cv2.imwrite(file, img)


for i in img_list:
    createImage(i.url, i.filename)
    file = "{}{}".format(image_source, i.filename)
    files.append(file)

result = DeepFace.verify(files[0], files[1])
print(result['verified'])
if (type(result['verified']) == bool):
    for i in files:
        if (os.path.isdir(i)):
            os.remove(i)
