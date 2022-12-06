from deepface import DeepFace
from retinaface import RetinaFace
import urllib.request
import cv2 as cv2
import numpy as np
import os

url = 'https://i0.wp.com/www.ghanacelebrities.com/wp-content/uploads/2021/11/261569341_130230356093601_7405743976020896106_n-1.jpg'
url2 = 'http://africa.cgtn.com/wp-content/photo-gallery/2016/12/Mahama-1.jpg'


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
        for count in faceCount:
            if (2*count != 2):
                valid = False
            else:
                valid = True
        return valid
    else:
        print('Something went wrong')


def checkResemblance():
    print(checkValidity())
    # if (len(files) == 2):
    #     for image in files:
    #         face = RetinaFace.detect_faces(img_path='./{}'.format(image))
    #         print(len(face))
    #         if (len(face) == 1):
    #             result = DeepFace.verify(
    #                 img1_path=files[0], img2_path=files[1], model_name='Facenet', distance_metric='euclidean')
    #             if (isinstance(result['verified'], bool)):
    #                 for i in files:
    #                     if (os.path.isdir('./{}'.format(i))):
    #                         print(i)
    #                         os.remove(i)
    #             print(result['verified'])
    #         else:
    #             print('Photo must contain only one person')


checkResemblance()
