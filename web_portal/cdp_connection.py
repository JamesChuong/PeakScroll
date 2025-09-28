import os
import json
import requests
import time
from websockets.sync.client import connect

class CDPConnection:
    def __init__(self, port=9222):
        self.port = port
        self.title = 'unknown'
        response = requests.get(f'http://localhost:{self.port}/json')
        ws_url = None
        
        for page in response.json():
            if 'instagram' in page['title'].lower():
                self.title = 'instagram'
                ws_url = page['webSocketDebuggerUrl']
                break
            elif 'youtube' in page['title'].lower():
                self.title = 'youtube'
                ws_url = page['webSocketDebuggerUrl']
                break

        if ws_url == None:
            raise ValueError()

        self.ws = connect(ws_url)
        self.msg_id = 0

        self.last_scrolled = time.perf_counter()

    def send_command(self, command):
        self.ws.send(command)
        response = json.loads(self.ws.recv())
        print(response)

    def scroll(self):
        # can only scroll after a two second cooldown
        if time.perf_counter() - self.last_scrolled < 2:
            return

        self.last_scrolled = time.perf_counter()

        command = {
            "id": self.msg_id,
            "method": "Input.dispatchMouseEvent",
            "params": {
                "type": "mouseWheel",
                "x": 500,
                "y": 500,
                "deltaX": 0,
                "deltaY": 512,
                "pointerType": "mouse"
            }
        }
        self.msg_id += 1
        self.send_command(json.dumps(command))

    def execute(self, script_or_filename):
        js_to_execute = script_or_filename
        filepath = f"./js/{script_or_filename}.js"

        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                js_to_execute = f.read()

        command = {
            "id": self.msg_id,
            "method": "Runtime.evaluate",
            "params": {
                "expression": js_to_execute
            }
        }
        self.msg_id += 1
        self.send_command(json.dumps(command))