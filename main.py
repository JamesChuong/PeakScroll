from collections import deque, Counter

import numpy as np
import cv2 as cv
from time import perf_counter
from deepface import DeepFace
from enum import Enum
from cdp_connection import CDPConnection


class EmotionDetector():
    emotion_buffer = deque(maxlen=10)

    def __init__(self):

        pass

    def analyze_emotions(self, file):

        conn = CDPConnection()
        last_scroll = perf_counter()
        face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
        npimg = np.frombuffer(file, np.uint8)
        frame = cv.imdecode(npimg, cv.IMREAD_COLOR)
        most_common_emotion = ""
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            # For single face, select the largest one (or implement other logic)
            (x, y, w, h) = max(faces, key=lambda rect: rect[2] * rect[3])  # Largest face by area

        else:

            (x, y, w, h) = faces[0]

        face_roi = frame[y:y + h, x:x + w]

        try:
            # Analyze emotions using deepface
            predictions = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
            if predictions:
                emotion = predictions[0]['dominant_emotion']
                self.emotion_buffer.append(emotion)

                # cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # cv.putText(frame, emotion, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                most_common_emotion = Counter(self.emotion_buffer).most_common(1)[0][0]

                # if current_emotion != most_common_emotion:
                #     current_emotion = emotion
                #     print(f"The emotion is {current_emotion}")

                if most_common_emotion == 'happy' and perf_counter() - last_scroll > 4:
                    last_scroll = perf_counter()
                    print(f"Scrolling because {most_common_emotion}")
                    conn.scroll()

        except Exception as e:
            # cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Mark problematic faces

            raise ValueError(f"Emotion analysis error: {e}")

        return most_common_emotion
