l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

def list(l1: list, l2: list) -> list:
    newList = l1[1: : 2] + l2[: : 2]
    return newList

l3 = list(l1, l2)
print("New list: ", l3)