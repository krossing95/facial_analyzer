from deepface import DeepFace
from retinaface import RetinaFace
import urllib.request
import cv2 as cv2
import numpy as np
import os

url = 'https://cdn.standardmedia.co.ke/sdemedia/sdeimages/monday/sxgbyjo4gzu8wp611a6b70ea417.jpg'
url2 = 'https://pbs.twimg.com/profile_images/1349055126665916419/OI3hQ25k_400x400.jpg'


class imgList:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename


img_list = []
img_list.append(imgList(url, 'obama1.png'))
img_list.append(imgList(url2, 'obama2.png'))

files = []
faceCount = []


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


def checkValidity():
    valid = False
    if (len(files) == 2):
        for image in files:
            face = RetinaFace.detect_faces(img_path='./{}'.format(image))
            faceCount.append(len(face))
        if (faceCount[0] == 1 and faceCount[len(faceCount)-1] == 1):
            valid = True
        return valid
    else:
        print('Something went wrong')


def checkResemblance():
    validity = checkValidity()
    if (validity == False):
        print('Please use images with only one person')
    elif (validity == True):
        result = DeepFace.verify(
            img1_path=files[0], img2_path=files[1], model_name='Facenet', distance_metric='euclidean')
        if (isinstance(result['verified'], bool)):
            for i in files:
                if (os.path.isdir('./{}'.format(i))):
                    print(i)
                    os.remove(i)
        print(result['verified'])


checkResemblance()
