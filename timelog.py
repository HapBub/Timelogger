from datetime import datetime

# Creating a text file with the command function "x"
# Appending if the file already exists

f = open ("/home/bubble/Timelogger/log.txt","a")

# Getting the current time

now = datetime.now()

# Hour, minute, second, day, month, year

date_str = now.strftime("%d/%m/%Y %H:%M:%S")

# Displaying output

print(date_str)
    
# Writing in the file

f.write (" " + date_str + " /n")

# Closing the file

f.close()


