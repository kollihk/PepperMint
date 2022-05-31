
# pip install OpenCV 
# pip install webbrowser ( built in )
# Run in CLI: python QR_Scanner_webcam.py

from more_itertools import one
import cv2
import webbrowser


cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

while True:
    _,img = cap.read()    
        # detect and decode
    data, one, _ = detector.detectAndDecode(img)
        # check if there is a QRCode in the image
    if data:
        a=data
        break
    cv2.imshow('QR CODE Scanner App', img)
    if cv2.waitKey(1) == ord('q'):
        break

b=webbrowser.open(str(a))
cap.release()
cv2.destroyAllWindows()

