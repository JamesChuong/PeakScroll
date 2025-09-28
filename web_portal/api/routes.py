
from flask import Blueprint, jsonify, request, Flask, render_template
import requests
import json
import websocket
from web_portal.emotion_detector import EmotionDetector
from web_portal.cdp_connection import CDPConnection
from web_portal.gesture_detector import GestureDetector

emotion_detector = EmotionDetector()

gesture_detector = GestureDetector()

conn = CDPConnection()

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route('/')
def home_page():
    return render_template('index.html')

@api_blueprint.route("/analyze_emotion", methods=["POST"])
def analyze_emotion():
    frame = request.files["frame"].read()

    gesture = gesture_detector.analyze_gestures(frame)
    emotion = emotion_detector.analyze_emotions(frame)

    print(f'Emotion is {emotion}, gesture is {gesture}.')

    if gesture == 'thumb_up' and conn.title == 'instagram':
        conn.execute('like')

    if emotion == 'happy' and conn.title == 'instagram':
        conn.execute('emoji')

    if gesture == 'thumb_down' or gesture == 'closed_fist':
        conn.scroll(512)

    if gesture == 'pointing_up':
        conn.scroll(-512)

    return jsonify({"emotion": emotion, "gesture": gesture})
