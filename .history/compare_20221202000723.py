from deepface import DeepFace
from retinaface import RetinaFace
import base64
import os


def personVerifier(fromWebcam, fromDB):
    capturedToMatch = """{}""".format(fromWebcam)
    dbFoundToMatch = """{}""".format(fromDB)

    def getFileExtension():
        ext = ''
        first_split = capturedToMatch.split(',')
        if (len(first_split) == 2):
            second_split = first_split[0].split('/')
            if (len(second_split) == 2):
                third_split = second_split[1].split(';')
                if (len(third_split) == 2):
                    ext = third_split[0]
        return ext

    ext = getFileExtension()

    def compareHumans():
        verification = False
        if (len(ext) > 0):
            file = './image.{}'.format(ext)
            if (os.path.exists(file)):
                os.remove(file)
            newcapturedToMatch = capturedToMatch.split(',')[1]
            base64Byte = newcapturedToMatch.encode('utf-8')
            with open('image.{}'.format(ext), 'wb') as imageFile:
                decoded_data = base64.decodebytes(base64Byte)
                imageFile.write(decoded_data)
            face = RetinaFace.detect_faces(img_path=file)
            if (len(face) == 1):

                result = DeepFace.verify(
                    capturedToMatch_path=capturedToMatch, img2_path=dbFoundToMatch, model_name='Facenet', distance_metric='euclidean')
                if (isinstance(result['verified'], bool)):
                    os.remove(file)
                    verification = result['verified']
            else:
                return 'Please use images with only one person'
        else:
            return 'Photo is missing'
        return verification
    return compareHumans()
