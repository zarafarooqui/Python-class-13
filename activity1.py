#OPEN FILE
file = open('Codingal.txt')

print(file.read())
file.close()

#write operation
file_write = open('Codingal.txt','w')

file_write.write("File in write mode...")
file_write.write("Hi! I am Penguin. I am 1 yr .old")
file_write.close()

#append operation
file_append = open('Codingal.txt','a')

file_append.write("File in write mode...")
file_append.write("Hi! I am Penguin. I am 1 yr .old")
file_append.close()