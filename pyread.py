"""This script reads a text file named as input.txt in user directory.
   A new output.txt file will be created with log data."""
import datetime
#Convert the standard timestamp into a string form
TIME_STAMP = str(datetime.datetime.utcnow())
#Open a file named input.txt from datadir in readmode
with open('/datadir/input.txt') as file_1, \
     open('/datadir/output.txt', 'w') as file_2:
    file_2.write(file_1.read())
#Write the time stamp content into a file
    file_2.write("\nLast executed on: ")
    file_2.write(TIME_STAMP)
