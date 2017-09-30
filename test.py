D = "UNR"
stat = open("/home/suraj/ESSP/status.txt","w+")
if(D == "UNR"):
  stat.write('''var="a"''')
else:
  stat.write('''var="c"''')
stat.close()

