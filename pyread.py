import datetime
print ("Hello CloudByte!!!")
print ("I am reading text files\n")
with open("/datadir/input.txt") as file:
	data = file.read()
	print(data)
	f= open("/datadir/output.txt","a")	
	st=str(datetime.datetime.utcnow())
	f.write("\n")
	f.write(data)
	print(st)	
	f.write("Last executed on: ")
	f.write(st)
	f.close()
