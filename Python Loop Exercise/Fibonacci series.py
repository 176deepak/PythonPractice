prev = 0
curr = 1
print("Fibonacci series: ")
print(prev, curr, end=" ")

for i in range(8):
    next = prev + curr
    print(next, end=" ")
    prev = curr
    curr = next
