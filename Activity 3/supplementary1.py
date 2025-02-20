# Try reading and writing a video file in various formats.
import cv2

cap = cv2.VideoCapture('OpenCV Crash Course/Activity_3_Python_Files/supple1_test.mp4')

if (cap.isOpened()== False):
    print("Error opening video file")

while(cap.isOpened()):
    
    ret, frame = cap.read()
    if ret == True:
    # Display the resulting frame
        cv2.imshow('Supplementary1', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == ord('q'):  # 27 = ESC key
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()