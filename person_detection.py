import cv2

def is_person_in_frame(frame):
    # Load the pre-trained Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Check if any faces were detected
    if len(faces) > 0:
        return True  # Person (face) is detected in the frame
    else:
        return False  # No person detected in the frame

# Example usage: Capture video from the webcam and check if a person is present
cap = cv2.VideoCapture(0)  # Use 0 for default webcam, change it to the appropriate camera index if using an external camera

while True:
    success, frame = cap.read()
    if not success:
        break

    person_detected = is_person_in_frame(frame)

    if person_detected:
        print("Person detected!")
    else:
        print("No person detected.")

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
