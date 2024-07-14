import cv2

faceclassifier = cv2.CascadeClassifier()
faceclassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    faces= faceclassifier.detectMultiScale(frame)
    for face in faces:
        x, y, w, h = face
        new_frame =cv2.rectangle(frame, (x, y), (x+w, y+h), color=(255,0,0), thickness=3)
    cv2.imshow('',frame)
    if (cv2.waitKey(30)==27):
        cap.release()
        cv2.destroyAllWindows()