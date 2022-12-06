from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from compare import personVerifier
from mail import transitAccVerification
import json

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/')
@cross_origin(supports_credentials=True)
def index():
    return "Hello And Welcome To SAS API"


@app.route('/sas/verifier', methods=['POST'])
def verifyPerson():
    data = request.get_json()
    fromWebcam, fromDB = data['from_webcam'], data['from_db']
    if (len(fromWebcam) == 0 or len(fromDB) == 0):
        return json({"error": "All fields are required"})
    else:
        result = personVerifier(fromWebcam, fromDB)
        if (isinstance(result, bool)):
            return json({"user_verification": bool(result)})
        else:
            return json({"error": str(result)})


@app.route('/sas/transit/vl', methods=['POST'])
def sendAccountVerificationLink():
    data = request.get_json()
    receiver, subject, link, name = data['receiver'], data['subject'], data['link'], data['name']
    if (len(receiver) == 0 or len(subject) == 0 or len(link) == 0 or len(name) == 0):
        return jsonify(error="All fields are required")
    linkSent = transitAccVerification(receiver, subject, link, name)
    if (linkSent != False):
        return json({"message": True})
    else:
        return json({"message": False})


if __name__ == "__main__":
    app.run()
