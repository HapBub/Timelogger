import sys
from datetime import datetime

# Creating a file with the command function "x"
# Appending if the file already exists

f = open ("/home/bubble/Timelogger/advancedlog.txt","a")

# Getting the current time

now = datetime.now()

# Hour, minute, second, day, month, year

date_str = now.strftime("[%d/%m/%Y %H:%M:%S] /n")

#Argument count

argc = len(sys.argv)

#Displaying output

while argc > 1:
    print("argument ~" , str(sys.argv[argc-1]))
    argc -= 1
if argc==1:
    print ("no arguments")

# Writing in the file

f.write (" " + date_str)    

# Closing the file

f.close()


