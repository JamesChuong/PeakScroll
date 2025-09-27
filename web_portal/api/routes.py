
from flask import Blueprint, jsonify, request, Flask, render_template
import requests
import json
import websocket
from web_portal.emotion_detector import EmotionDetector
from web_portal.cdp_connection import CDPConnection

emotion_detector = EmotionDetector()

conn = CDPConnection()

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route('/')
def home_page():
    return render_template('index.html')

@api_blueprint.route("/analyze_emotion", methods=["POST"])
def analyze_emotion():
    frame = request.files["frame"].read()

    most_common_emotion = emotion_detector.analyze_emotions(frame)
    
    # if most_common_emotion != 'neutral' and most_common_emotion != 'happy':
    #     conn.scroll()
        
    if most_common_emotion == 'happy':
        conn.execute('emoji')

    # if most_common_emotion == 'happy':
    #     conn.execute('like')
    
    return jsonify({"emotion": most_common_emotion})
