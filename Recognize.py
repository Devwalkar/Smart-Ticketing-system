import cv2
import time
import os
#import subprocess

def detect(train,test):
# Initiate SIFT detector
    sift = cv2.SIFT()
# find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(train,None)
    kp2, des2 = sift.detectAndCompute(test,None)

# FLANN parameters
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   

    flann = cv2.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(des1,des2,k=2)
    y=0

    for i,(m,n) in enumerate(matches):
        if m.distance < 0.60*n.distance:
           y = y+1           
    return y       


index = 0
start = True
while(start):
   index+=1
   if(os.path.isdir("/home/suraj/ESSP/train_faces/s"+str(index)) == False):
     start = False



NoUser = index-1 
z=[]
X = os.getcwd()
os.chdir(X+"/test_faces")
test = cv2.imread('test.png',0)
#clahe = cv2.createCLAHE(clipLimit=2.0)
#test = clahe.apply(test)

for i in xrange(NoUser):
    os.chdir(X+"/train_faces/s"+str(i+1))
    train= cv2.imread('train.png',0)          # trainImage
#    cv2.imshow("train",train)
 #   train= clahe.apply(train) 
    y=detect(train,test)
    z.append(y)
    os.chdir(X) 

#cv2.imshow("test",test)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Recognizing ID    
ID= (z.index(max(z)))+1
if max(z)<=1:
    D = "UNR"
    print "User not recognized"
else:
   if ID==1:
      D = "suraj"                     
   if ID==2:
      D = "omkar"


stat = open("/home/suraj/ESSP/status.txt","w+")
if(D == "UNR"):
  stat.write('''var="a"''')
else:
  stat.write('''var="c"''')
stat.close()


F = open("SourceStation.txt","r+")
A = F.read()
F.close()

F = open("DestStation.txt","r+")
B = F.read()
F.close()

F = open("SourceStation.txt","w+")
F.write("")
F.close()
F = open("DestStation.txt","w+")
F.write("")
F.close()   

Fn = open("/home/suraj/ESSP/trial.txt","w+")
if D=="UNR":
    E = D+"///"
else:
    E = D + "/" + A + "/" + B + "/ "
Fn.write(E)
Fn.close()

print E
time.sleep(2)


'''


#f = open("/opt/lampp/htdocs/filew.txt","w")
#f.writelines(E)
#f.close()
  

# This file is used to make main.sh script to wait until face recognition is complete
#Fil = open("temp.txt","w+")
#Fil.write("temp")
#Fil.close()




#os.system("rm -f /home/suraj/ESSP/status.txt")
os.system("rm -f /home/suraj/ESSP/test_faces/test.png")
#os.system("rm -f /home/suraj/ESSP/temp.txt")
os.system('echo "after removing"')
time.sleep(2)
print "before sending"
os.system('scp /home/suraj/ESSP/status.txt pi@10.42.0.195:/home/pi/ESSP')
print "after sending"
if D!="UNR":  
  os.system("php /opt/lampp/htdocs/file.php")
  os.system("chromium-browser localhost/file.php")
  os.system('wmctrl -a "Google Chrome"; xdotool key Ctrl+w; wmctrl -r "Google Chrome" -b add,shaded')
  
subprocess.call("./check.sh", shell=True)



'''





