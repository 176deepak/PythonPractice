num = int(input("Enter number of numbers: "))
start = 1
sum_seq = 0

for i in range(0, num):
    print(start, end=" ")
    sum_seq += start
    start = start * 10 + 1
print("\nSum of above series is:", sum_seq)