from flask import Blueprint, jsonify, request, Flask
import requests
import json
import websocket

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from API!"})

