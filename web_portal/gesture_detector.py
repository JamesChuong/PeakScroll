import cv2 as cv
import mediapipe as mp
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode
PoseLandmarkerResult = mp.tasks.vision.PoseLandmarkerResult

options = GestureRecognizerOptions(
        base_options=BaseOptions(model_asset_path="../models/gesture_recognizer.task"))

class GestureDetector():
    def __init__(self):
        self.gesture_recognizer = GestureRecognizer.create_from_options(options)

    def analyze_gestures(self, file):
        # Convert bytes to NumPy array
        np_array = np.frombuffer(file, np.uint8)
        image_bgr = cv.imdecode(np_array, cv.IMREAD_COLOR)
        image_rgb = cv.cvtColor(image_bgr, cv.COLOR_BGR2RGB)

        # Create MediaPipe Image
        mp_image = mp.Image(mp.ImageFormat.SRGB, image_rgb)
        
        #mp_image = mp.Image(mp.ImageFormat.SRGB, file)
        result = self.gesture_recognizer.recognize(mp_image)
        
        try:
            return result.gestures[-1][0].category_name.lower()

        except Exception as e:
            return 'none'