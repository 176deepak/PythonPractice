num = int(input("Enter number: "))
factorial = 1

while num != 0:
    factorial = factorial*num
    num -= 1

print("Factorial: ", factorial)