num = int(input("Enter number: "))
rem = 0

while num != 0:
    rem = num % 10 + (rem)*10
    num = num//10

print("Integer in reverse order: ", rem)