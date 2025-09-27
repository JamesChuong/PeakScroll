from flask import Blueprint, jsonify, request, render_template
from web_portal import main

emotion_detector = main.EmotionDetector()

api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from API!"})


@api_blueprint.route('/')
def home_page():
    return render_template('index.html')


@api_blueprint.route("/analyze_emotion", methods=["POST"])
def analyze_emotion():

    req = request.get_json(silent=True)

    frame = req["frame"].read()

    most_common_emotion = emotion_detector.analyze_emotions(frame)

    return jsonify({"emotion": most_common_emotion})




