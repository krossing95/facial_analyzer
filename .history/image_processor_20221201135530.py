from deepface import DeepFace
import urllib.request
import cv2 as cv2
import numpy as np
import os

url = 'https://upload.wikimedia.org/wikipedia/commons/5/59/Pete-edochie.jpg'
url2 = 'https://www.primebusiness.africa/wp-content/uploads/2022/07/60d9bb9241b8b.jpg'


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
        getImage(i.url, i.filename)
        files.append(i.filename)
    return files


callImage()


def checkResemblance():
    if (len(files) == 2):
        result = DeepFace.verify(files[0], files[1])
        if (isinstance(result['verified'], bool)):
            for i in files:
                if (os.path.isdir(i)):
                    print(i)
                    os.remove(i)
        print(result['verified'])


checkResemblance()
