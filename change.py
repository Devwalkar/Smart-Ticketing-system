import cv2
import numpy as np
import Image
import os


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



index = 0
start = True

while(start):
   index+=1
   if(os.path.isdir("/home/suraj/ESSP/train_faces/s"+str(index)) == False):
     start = False

# index = 6
for i in range(1,index):
  img = cv2.imread("/home/suraj/ESSP/train_faces/s"+str(i)+"/train.png")
  img2 = equalizergb(img)
  im = Image.fromarray(img2)
  im.save("/home/suraj/ESSP/train_faces/s"+str(i)+"/train2.png")
  print "done "+str(i)
     
  




