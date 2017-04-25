print ("Hello CloudByte!!!")
print ("I am reading the contents from different text files\n")
#The testfiles are present in the same directory as of readtext.py file
with open("testfile1.txt") as f1:
	print(f1.read())
with open("testfile2.txt") as f2:
	print(f2.read())
with open("testfile3.txt") as f3:
	print(f3.read())
# To read the files from your local direcctories
with open("/path/to/your/local/file.txt") as f:
	print(f.read())
