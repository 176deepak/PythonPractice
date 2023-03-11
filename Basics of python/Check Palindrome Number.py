num1 = input("Enter number to check palindrome: ")
num2 = num1[-1::-1]


if int(num1) == int(num2):
    print("Number is plaindrome.")
else:
    print("Number is not plaindrome.")