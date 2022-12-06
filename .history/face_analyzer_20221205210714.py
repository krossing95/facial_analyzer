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
    if (ext.lower() == 'jpeg' or ext.lower() == 'png'):
        return ext
    else:
        ext = ''
        return ext


def createImageFile(base64Path):
    file = './{}.{}'.format(IMAGE_ID, getFileExtension(base64Path))
    newcapturedToMatch = base64Path.split(',')[1]
    base64Byte = newcapturedToMatch.encode('utf-8')
    with open(file, 'wb') as imageFile:
        decoded_data = base64.decodebytes(base64Byte)
        imageFile.write(decoded_data)
    return True


def faceDetector(base64Path):
    file = './{}.{}'.format(IMAGE_ID, getFileExtension(base64Path))
    face = RetinaFace.detect_faces(img_path=file)
    return len(face)


def faceVerifier(imgPath1, imgPath2):
    result = DeepFace.verify(img1_path=imgPath1, img2_path=imgPath2,
                             model_name='Facenet', distance_metric='euclidean')
    if (isinstance(result['verified'], bool)):
        return result['verified']
    else:
        return 'Error detected'


def personVerifier(fromWebcam, fromDB):
    capturedToMatch = """{}""".format(fromWebcam).strip()
    dbFoundToMatch = """{}""".format(fromDB).strip()

    ext = getFileExtension(base64Path=capturedToMatch)

    def compareHumans():
        verification = False
        if (len(ext) > 0):
            createImageFile(base64Path=capturedToMatch)
            faceCount = faceDetector(base64Path=capturedToMatch)
            if (faceCount == 1):
                os.remove('./{}.{}'.format(IMAGE_ID, ext))
                result = faceVerifier(
                    imgPath1=capturedToMatch, imgPath2=dbFoundToMatch)
                if (isinstance(result, bool)):
                    verification = result
                else:
                    return 'Ouch! Something went wrong'
            else:
                return 'Please use images with only one person'
        else:
            return 'Photo is missing'
        return verification
    return compareHumans()


def verifyImageExistence(personsList, fromWebcam):
    capturedToMatch = """{}""".format(fromWebcam).strip()

    ext = getFileExtension(base64Path=capturedToMatch)

    def verifyPersonExistence():
        existence = False
        if (len(ext) > 0):
            faceCount = faceDetector(base64Path=capturedToMatch)
            if (faceCount == 1):
                for face in personsList:
                    faceToMatch = """{}""".format(face).strip()
                    result = faceVerifier(
                        imgPath1=faceToMatch, imgPath2=capturedToMatch)
                    if (isinstance(result, bool)):
                        existence = result
                        if (existence == True):
                            break
                    else:
                        return 'Ouch! Something went wrong'
        return existence
    return verifyPersonExistence()
