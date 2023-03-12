str1 = "PyNaTive"
lower = ""
upper = ""

for i in str1:
    if i.islower():
        lower = lower + i
    else:
        upper = upper + i

string = lower + upper
print("string: ", string)