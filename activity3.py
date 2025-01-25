firstfile = input("Enter the name of  first file")
secondfile = input("Enter the name of second file")

f1 = open(firstfile,'a')
f2 = open(secondfile,'r')
#appending contents into another file
f1.write(f2.read())

#relocating the cursor
f1.seek(0)
f2.seek(0)


f1 = open(firstfile,'r')
f2 = open(secondfile,'r')

#printing the contents
print('content of first file after appending - \n' , f1.read())
print('content of second file after appending - \n' , f2.read())

#closing the file
f1.close()
f2.close()
