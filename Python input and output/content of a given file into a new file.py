
with open("file1.txt", "r") as reader:
    lines = reader.readlines()

with open("file2.txt", mode="w") as writer:
    flag = 0

    for line in lines:
        if flag != 4:
            writer.write(line)
        
        flag += 1

        