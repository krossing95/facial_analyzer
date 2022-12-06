from deepface import DeepFace
from retinaface import RetinaFace
import base64
import uuid
import os

IMAGE_ID = uuid.uuid4()


def getFileExtension(base64Path):
    ext = ''
    first_split = base64Path.split(',')
    if (len(first_split) > 1):
        second_split = first_split[0].split('/')
        if (len(second_split) > 1):
            third_split = second_split[1].split(';')
            if (len(third_split) > 1):
                ext = third_split[0]
    return ext


def createImageFile(base64Path):
    file = './{}.{}'.format(IMAGE_ID, getFileExtension(base64Path))
    newcapturedToMatch = base64Path.split(',')[1]
    base64Byte = newcapturedToMatch.encode('utf-8')
    with open(file, 'wb') as imageFile:
        decoded_data = base64.decodebytes(base64Byte)
        imageFile.write(decoded_data)


def personVerifier(fromWebcam, fromDB):
    capturedToMatch = """{}""".format(fromWebcam)
    dbFoundToMatch = """{}""".format(fromDB)

    ext = getFileExtension()

    def compareHumans():
        verification = False
        if (len(ext) > 0):
            file = './{}.{}'.format(IMAGE_ID, ext)
            createImageFile(base64Path=capturedToMatch)
            face = RetinaFace.detect_faces(img_path=file)
            if (len(face) == 1):
                result = DeepFace.verify(
                    img1_path=capturedToMatch, img2_path=dbFoundToMatch, model_name='Facenet', distance_metric='euclidean')
                if (isinstance(result['verified'], bool)):
                    os.remove(file)
                    verification = result['verified']
            else:
                return 'Please use images with only one person'
        else:
            return 'Photo is missing'
        return verification
    return compareHumans()
