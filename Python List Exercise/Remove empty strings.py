list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

def remove_none(l:list):
    res = list(filter(None, l))
    return res

print("Original list: ",list1)

res = remove_none(list1)

print("filtered list: ", res)
