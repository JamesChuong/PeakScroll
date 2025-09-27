from collections import deque, Counter

import numpy as np
import cv2 as cv
from time import perf_counter
from deepface import DeepFace
from enum import Enum

from cdp_connection import CDPConnection

cap = cv.VideoCapture(0)

conn = CDPConnection()

last_scroll = perf_counter()

class Emotions(Enum):
    HAPPY = 1
    SAD = 2
    NEUTRAL = 3
    ANGRY = 4


face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

current_emotion = ""

emotion_buffer = deque(maxlen=10)  # about 1 sec if 30fps

# frame_count = 0

# skip_frame = 3

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:

        continue

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
            emotion_buffer.append(emotion)

            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(frame, emotion, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            most_common_emotion = Counter(emotion_buffer).most_common(1)[0][0]

            # if current_emotion != most_common_emotion:
            #     current_emotion = emotion
            #     print(f"The emotion is {current_emotion}")

            if most_common_emotion == 'happy' and perf_counter() - last_scroll > 4:
                last_scroll = perf_counter()
                print(f"Scrolling because {most_common_emotion}")
                conn.scroll()

    except Exception as e:
        print(f"Emotion analysis error: {e}")
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Mark problematic faces

    cv.imshow('Emotion Detection', frame)

    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
