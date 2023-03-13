list1 = [54, 44, 27, 79, 91, 41]

def list(l: list) -> list:
    ele_4 = l.pop(4)
    l[2] = ele_4
    l[-1] = ele_4

    return l

list = list(list1)
print("Updated list: ", list)