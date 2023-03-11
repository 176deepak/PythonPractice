a, b = input("Enter start & end range value: ").split()

print("Prime numbers within range: ")
for i in range(int(a), int(b)+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
