import os

size = os.stat("file1.txt").st_size

if size == 0:
    print("File is empty.")
else:
    print("File is not empty.")