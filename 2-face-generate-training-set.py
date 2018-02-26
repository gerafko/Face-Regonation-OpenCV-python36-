import cv2

#filename = r'c:\projects\python\anton-goryunov-diploma\images\v4.mp4'

def generate():
  face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
  eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')
  print(face_cascade.empty())
  print(eye_cascade.empty())
  camera = cv2.VideoCapture(0)
  #camera = cv2.VideoCapture(filename)
  count = 0
  while (True):
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(300,300))
    
    for (x,y,w,h) in faces:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
        f = cv2.resize(gray[y:y+h, x:x+w], (200, 200))

        cv2.imwrite('./training-set-anton/%s.pgm' % str(count), f)
        #print count
        count += 1

    cv2.imshow("camera", frame)
    if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
      break

  camera.release()
  cv2.destroyAllWindows()

if __name__ == "__main__": 
  generate()
