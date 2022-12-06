from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from face_analyzer import personVerifier, verifyImageExistence
from mail import transitAccVerification

app = Flask(__name__)
CORS(app, support_credentials=True)

ROUTE_PREFIX = '/sas/'


@app.route('/')
@cross_origin(supports_credentials=True)
def index():
    return "Hello And Welcome To SAS API"


@app.route('{}verifier'.format(ROUTE_PREFIX), methods=['POST'])
def verifyPerson():
    data = request.get_json()
    fromWebcam, fromDB = data['from_webcam'], data['from_db']
    if (len(fromWebcam) == 0 or len(fromDB) == 0):
        return jsonify(error="All fields are required")
    else:
        result = personVerifier(fromWebcam, fromDB)
        if (isinstance(result, bool)):
            return jsonify(user_verification=bool(result))
        else:
            return jsonify(error=str(result))


@app.route('{}mass_verification'.format(ROUTE_PREFIX), methods=['POST'])
def massFacialVerification():
    data = request.get_json()
    fromWebcam, personsList = data['from_webcam'], data['from_db']
    if (len(fromWebcam) != 1 or len(personsList) == 0 or isinstance(personsList, list) == False):
        return jsonify(error=False)
    else:
        result = verifyImageExistence(personsList, fromWebcam)
        if (isinstance(result, bool)):
            return jsonify(existence=bool(result))
        else:
            return jsonify(error=str(result))


@app.route('{}transit/vl'.format(ROUTE_PREFIX), methods=['POST'])
def sendAccountVerificationLink():
    data = request.get_json()
    receiver, subject, link, name = data['receiver'], data['subject'], data['link'], data['name']
    if (len(receiver) == 0 or len(subject) == 0 or len(link) == 0 or len(name) == 0):
        return jsonify(message=False)
    linkSent = transitAccVerification(receiver, subject, link, name)
    if (linkSent != False):
        return jsonify(message=True)
    else:
        return jsonify(message=False)


if __name__ == "__main__":
    app.run()
