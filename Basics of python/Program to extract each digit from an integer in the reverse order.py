s = input("Enter number: ")
i = len(s)
num = int(s)

while num != 0:
    print(i,"location digit: ", num%10)
    num = num//10
    i -= 1