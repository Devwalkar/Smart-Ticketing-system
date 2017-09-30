clear
if find /home/suraj/ESSP/test_faces -maxdepth 0 -empty | read v; 
 then echo "Error occured:No image available"; 
else 
 
 echo "Recognizing image....."; 
    python /home/suraj/ESSP/Recognize.py
  
 #while [ ! -f /home/suraj/ESSP/temp.txt ]
 # do
 #  echo "a"
 # done
  
  sleep 1
  #scp /home/suraj/ESSP/status.txt pi@10.42.0.195:/home/pi/ESSP
#  rm -f /home/suraj/ESSP/status.txt
#  rm -f /home/suraj/ESSP/test_faces/test.png
#  rm -f /home/suraj/ESSP/temp.txt
#  echo "after removing" 
#  php /opt/lampp/htdocs/file.php 
#  chromium-browser localhost/file.php 
#  wmctrl -a "Google Chrome"; xdotool key Ctrl+w; wmctrl -r "Google Chrome" -b add,shaded

#   source /home/suraj/ESSP/check.sh
fi
