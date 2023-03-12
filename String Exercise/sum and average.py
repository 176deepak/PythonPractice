def sum_average(str:str):
    sum = 0
    n = 0
    for i in str:
        if i.isdigit():
            sum += int(i)
            n += 1
    
    print("Sum is: ", sum)
    print("Average is: ", sum/n)

sum_average("PYnative29@#8496")