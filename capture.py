import cv2
import Image
import numpy as np

def equalizergb(image):
  bb = image[:,:,0]
  gg = image[:,:,1]
  rr = image[:,:,2]

  new = np.zeros((image.shape[0],image.shape[1],3) , 'uint8')
  new[:,:,0] = bb
  new[:,:,1] = gg
  new[:,:,2] = rr
  
  new2 = np.zeros((image.shape[0],image.shape[1],3) , 'uint8')
  bb2 = cv2.equalizeHist(bb)
  gg2 = cv2.equalizeHist(gg)
  rr2 = cv2.equalizeHist(rr)
  new2[:,:,0] = bb2
  new2[:,:,1] = gg2
  new2[:,:,2] = rr2
  return new2


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
  ret,frame = cap.read()
  if(ret == True):
      gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      gray = cv2.equalizeHist(gray)
      faces = face_cascade.detectMultiScale(gray,1.2,5)
      for(x,y,w,h) in faces:
         if(w>=0):
          cv2.rectangle(gray,(x,y-70),(x+w,y+h+30),(255,0,0),2)
          roi = frame[y-70:y+h+30, x:x+w] 
          cv2.imshow('roi',roi)

      cv2.imshow("frame",gray)
  c = cv2.waitKey(30) 
  if(c & 0xFF == ord('c')):
        resized = cv2.resize(roi,(200,200))
        im = Image.fromarray(resized)
        im.save("/home/suraj/ESSP/test_faces/test.png")
        break
'''
while True:
  ret,frame = cap.read()
  if(ret == True):
        cv2.imshow("img",frame)
        c = cv2.waitKey(30) 
        if(c & 0xFF == ord('c')):
          im = Image.fromarray(frame)
          im.save("/home/suraj/ESSP/test_faces/test.png")
          break

'''
cap.release()
cv2.destroyAllWindows()
