import cv2

cap = cv2.VideoCapture(0) # a VideoCapture object to acces webcam

# loading haar cascade classifier for face and body detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")

# infinte loop that reads continous frames
while True: 
    _, frame = cap.read() # reads frames from webcam

    #converts frame into grayscale to detect face
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #draws rectangle over detected face in each frame
    for (x, y, width, height) in faces:
       cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

    #display
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()