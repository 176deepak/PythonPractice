# Decimal number to octal number

num = int(input("Enter decimal number: "))
rem = 0
i = 1

while(num != 0):
    rem += (num%8)*i
    num = num//8
    i *= 10

print("Octal number is: ", rem)