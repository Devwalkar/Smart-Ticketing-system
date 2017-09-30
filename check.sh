#!/bin/bash
pc=0
clear
echo "Waiting for image....."
while [ ! -f /home/suraj/ESSP/test_faces/test.png ]
  do
    pc=$((pc%100))
    echo -ne "\r\033[0K${pc}%"
    sleep 1
    ((pc++))
  done
echo


source /home/suraj/ESSP/main.sh
