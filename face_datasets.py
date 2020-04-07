import cv2
import os
def assure_path_exists(path):
 dir = os.path.dirname(path)
 if not os.path.exists(dir):
  os.makedirs(dir)

cam = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = 4
count = 0
assure_path_exists("dataset/")


while True:
 # Read the video frame
 ret, tm =cam.read()
 # Convert the captured frame into grayscale
 gray = cv2.cvtColor(tm,cv2.COLOR_BGR2GRAY)
 # Get all face from the video frame
 faces = face_detector.detectMultiScale(gray, 1.2,5)
 # For each face in faces
 for(x,y,w,h) in faces:
 # Create rectangle around the face
  cv2.rectangle(tm, (x,y), (x+w,y+h), (0,255,0), 5)
  count +=1
  cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg",gray[y:y+h,x:x+w])
 cv2.imshow('frame', tm)  
 # If 'q' is pressed, close program
 if cv2.waitKey(100) & 0xFF == ord('q'):
   break

 elif  count>100:
     break



# Stop the camera
cam.release()
# Close all windows
cv2.destroyAllWindows()


      
