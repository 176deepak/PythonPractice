list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

def concat(l1:list, l2:list, size:int)->list:
    new_list = []
    for i in range(size):
        ele = l1[i]+l2[i]
        new_list.append(ele)

    return new_list

concat_list = concat(list1, list2, 4)

print("Two lists: ",list1,"& ",list2)
print("New list: ", concat_list)