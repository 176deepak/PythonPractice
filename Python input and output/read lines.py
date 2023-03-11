with open("file1.txt", "r") as reader:
    lines = reader.readlines()
    print(lines[3])