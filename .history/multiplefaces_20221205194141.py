from faces import faces, fromWebcam
from deepface import DeepFace
import uuid

for face in faces:
    result = DeepFace.verify(img1_path=face, img2_path=fromWebcam,
                             model_name='Facenet', distance_metric='euclidean')
    print(result, uuid.uuid4())
    if (result['verified'] == True):
        print('person already in db')
    else:
        print('Continue to save student')
