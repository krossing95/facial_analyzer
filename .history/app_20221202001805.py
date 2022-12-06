from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from compare import personVerifier

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/')
@cross_origin(supports_credentials=True)
def index():
    return "Hello And Welcome To Face Verifier"


@app.route('/sas/verifier', methods=['POST'])
def verifyPerson():
    data = request.get_json()
    fromWebcam, fromDB = data['from_webcam'], data['from_db']
    if (len(fromWebcam) == 0 or len(fromDB) == 0):
        return jsonify({"error": "All fields are required"})
    else:
        result = personVerifier(fromWebcam, fromDB)
        if (isinstance(result, bool)):
            return jsonify({"user_verification": bool(result)})
        else:
            return jsonify({"error": str(result)})


if __name__ == "__main__":
    app.run()
