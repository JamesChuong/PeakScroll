import json
import requests
import time
from websockets.sync.client import connect

class CDPConnection:
    def __init__(self, port=9222):
        self.port = port
        response = requests.get(f'http://localhost:{self.port}/json')
        ws_url = None
        
        for page in response.json():
            if 'instagram' in page['title'].lower():
                ws_url = page['webSocketDebuggerUrl']
                break
            elif 'youtube' in page['title'].lower():
                ws_url = page['webSocketDebuggerUrl']
                break

        if ws_url == None:
            raise ValueError()

        self.ws = connect(ws_url)
        self.msg_id = 0

    def send_command(self, command):
        self.ws.send(command)
        response = json.loads(self.ws.recv())
        print(response)

    def scroll(self):
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
