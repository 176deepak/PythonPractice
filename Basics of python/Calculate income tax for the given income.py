income = int(input("Enter income: "))

if income < 10000:
    print("No tax.")
elif income > 10000 and income <= 20000:
    tax = (10000*10)//100
    print("Payble tax: ", tax)
elif income > 20000:
    tax = (10000*10)//100 + ((income-20000)*20)//100
    print("Payble tax: ", tax)