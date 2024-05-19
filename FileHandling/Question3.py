#How to check file size in Python

#Using os module
import os

size_of_file=os.path.getsize("file.txt")
print(str(size_of_file) + ' bytes')