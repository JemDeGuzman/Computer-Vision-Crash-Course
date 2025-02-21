import cv2

def detect():
    face_cascade = cv2.CascadeClassifier(r'OpenCV Crash Course/Activity_6_Python_Files/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(r'OpenCV Crash Course/Activity_6_Python_Files/haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier(r'OpenCV Crash Course/Activity_6_Python_Files/haarcascade_smile.xml')

    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = camera.read()
        if not ret:
            print("Error: Failed to capture image.")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue box for face
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            try:
                eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)  # Green box for eyes
            except cv2.error:
                pass

            try:
                smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=20, minSize=(25, 25))
                for (sx, sy, sw, sh) in smiles:
                    cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)  # Red box for smile
            except cv2.error:
                pass

        cv2.imshow("Face, Eye & Smile Detection", frame)

        # Press 'q' or 'ESC' to exit
        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == ord('q'):  # 27 = ESC key
            break

    # Cleanup
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect()
