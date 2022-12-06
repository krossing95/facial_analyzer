from faces import faces, fromWebcam
from deepface import DeepFace


for face in faces:
    result = DeepFace.verify(img1_path=face, img2_path=fromWebcam,
                             model_name='Facenet', distance_metric='euclidean')
    print(result)
    if (result['verified'] == True):
        print('person already in db')
        break
    else:
        print('Continue to save student')
