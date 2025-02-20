# Capture video from your webcam and display on a window. Afterwards, the video should be written as a new file.

import cv2
import time

clicked = False

cameraCapture = cv2.VideoCapture(0)
fps = 30 # an assumption

size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

cameraCapture = cv2.VideoCapture(0)  # Open webcam
cv2.namedWindow('Supplementary3')
cv2.setMouseCallback('Supplementary3', onMouse)

print('Showing camera feed. Click window or press "q" or "ESC" to stop.')

videoWriter = cv2.VideoWriter(
    'OpenCV Crash Course/Activity_3_Python_Files/supple3_vid.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'),
    fps, size)


while cameraCapture.isOpened() and not clicked:
    success, frame = cameraCapture.read()
    videoWriter.write(frame)
    if not success:
        break
    
    cv2.imshow('Supplementary3',frame)  # Use cv2_imshow() instead of cv2.imshow()

    # Small delay to prevent excessive output
    time.sleep(0.05)

    # Stop when user presses 'q' or ESC
    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):  # 27 = ESC key
        break
    
cameraCapture.release()
cv2.destroyAllWindows()