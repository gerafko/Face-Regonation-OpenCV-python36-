import cv2

filename = r'c:\projects\python\anton-goryunov-diploma\images\v2.mp4'

def detect():
  face_cascade = cv2.CascadeClassifier(r'C:\projects\python\diploma\cascades\haarcascade_frontalface_default.xml')
  eye_cascade = cv2.CascadeClassifier(r'C:\projects\python\diploma\cascades\haarcascade_eye.xml')
  camera = cv2.VideoCapture(0)
  #camera = cv2.VideoCapture(filename)
  while (True):
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #img = cv2.imread(frame)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
        roi_gray = gray[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, 0, (40,40))
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(img,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(0,255,0),2)

    cv2.imshow("camera", frame)

    #cv2.waitKey(1000 / 12)
    
    if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
      break

  camera.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  detect()
