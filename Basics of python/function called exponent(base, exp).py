def exponent(base, exp):
    return base**exp

b = int(input("Enter base value: "))
e = int(input("Enter exponent value: "))

result = exponent(b,e)
print("Result: ", result)