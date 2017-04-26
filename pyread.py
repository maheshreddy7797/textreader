print ("Hello CloudByte!!!")
print ("I am reading text files\n")
with open("/datadir/test.txt") as file:
	print(file.read())
