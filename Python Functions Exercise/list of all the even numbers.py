def evenList(min, max):
    list = []
    for i in range(min, max):
        if i%2 == 0:
            list.append(i)
    print(list)

evenList(4, 30)