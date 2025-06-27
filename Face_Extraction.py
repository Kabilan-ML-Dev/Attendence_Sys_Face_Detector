import cv2
from mtcnn import MTCNN
import numpy as np

# Initialize webcam and face detector
cap = cv2.VideoCapture(0)
detector = MTCNN()

face_img = None  # To store detected face
face_saved = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to read frame from webcam.")
        break

    image = frame.copy()
    faces = detector.detect_faces(frame)

    if faces:
        for face in faces:
            if face['confidence'] >= 0.90:
                x, y, w, h = face['box']
                x, y = max(x, 0), max(y, 0)
                x2, y2 = x + w, y + h

                # Crop face safely
                if x2 > x and y2 > y:
                    face_img = frame[y:y2, x:x2]
                    # Draw rectangle
                    cv2.rectangle(image, (x, y), (x2, y2), (0, 255, 0), 2)
                    print("✅ Face detected and ready to save.")
                else:
                    print("⚠️ Invalid face box detected.")
                break  # Use only the first good detection
    else:
        face_img = None  # Reset if no face

    cv2.imshow("Capture", image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        if face_img is not None:
            try:
                face_resized = cv2.resize(face_img, (224, 224))
                face_array = face_resized / 255.0
                np.save("extracted_face1.npy", face_array)
                print("✅ Face saved as 'extracted_face1.npy'")
                face_saved = True
            except Exception as e:
                print("❌ Error during face crop or resize:", e)
        else:
            print("⚠️ No face detected to save. Try again.")
        break

    elif key == ord('q'):
        print("👋 Exiting without saving.")
        break

cap.release()
cv2.destroyAllWindows()

if not face_saved:
    print("⚠️ Face was not saved.")

