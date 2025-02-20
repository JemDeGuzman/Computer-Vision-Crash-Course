import cv2
import time

clicked = False

def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

cameraCapture = cv2.VideoCapture(0)  # Open webcam
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)

print('Showing camera feed. Click window or press "q" or "ESC" to stop.')

while cameraCapture.isOpened() and not clicked:
    success, frame = cameraCapture.read()
    if not success:
        break

    cv2.imshow('MyWindow',frame)  # Use cv2_imshow() instead of cv2.imshow()

    # Small delay to prevent excessive output
    time.sleep(0.05)

    # Stop when user presses 'q' or ESC
    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):  # 27 = ESC key
        break

cameraCapture.release()
cv2.destroyAllWindows()