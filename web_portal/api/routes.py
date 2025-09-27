from flask import Blueprint, jsonify, request, Flask, render_template
import requests
import json
import websocket
from web_portal.emotion_detector import EmotionDetector

emotion_detector = EmotionDetector()

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




