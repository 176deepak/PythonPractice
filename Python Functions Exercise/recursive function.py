def recursive(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        sum = num + recursive(num - 1)

    return sum

res = recursive(10)

print("Total sum: ", res)
