import cv2 as cv
from deepface import DeepFace

class EmotionDetector():
    def __init__(self):
        self.face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # returns string: 'happy', 'neutral', ...
    def analyze_emotions(self, file):
        gray = cv.cvtColor(file, cv.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            # For single face, select the largest one (or implement other logic)
            (x, y, w, h) = max(faces, key=lambda rect: rect[2] * rect[3])  # Largest face by area
        elif len(faces) == 0:
            return 'neutral'
        else:
            (x, y, w, h) = faces[0]

        face_roi = file[y:y + h, x:x + w]

        try:
            # Analyze emotions using deepface
            predictions = DeepFace.analyze(
                face_roi,
                actions=['emotion'],
                enforce_detection=False,
                model_name='Facenet512'
            )
            if predictions:
                return predictions[0]['dominant_emotion']

        except Exception as e:
            print(f"Ignoring exception: {e}")
            return 'neutral'
