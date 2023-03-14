list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

def concate(l1:list, l2:list)->list:
    new_list=[]
    for i in l1:
        for j in l2:
            ele = i+" "+j
            new_list.append(ele)
    return new_list

print("Two lists: ",list1,"&",list2)

new_list = concate(list1, list2)

print("New list: ",new_list)