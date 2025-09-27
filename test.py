import cv2

# Create a VideoCapture object for the default webcam (index 0)
cap = cv2.VideoCapture(0)

# Check if the webcam was opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # If frame reading was unsuccessful, break the loop
    if not ret:
        print("Error: Failed to read frame.")
        break

    # Display the captured frame
    cv2.imshow('Live Webcam Feed', frame)

    # Wait for 1 millisecond and check for 'q' key press to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()