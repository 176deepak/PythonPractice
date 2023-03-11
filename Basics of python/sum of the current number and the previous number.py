# sum of the current number and the previous number(range 10)
sum = 0

for i in range(10):
    print("Previous number",i-1,"and current number",i,"Sum: ", sum+i)
    sum = i
