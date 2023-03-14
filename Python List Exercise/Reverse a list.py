list1 = [100, 200, 300, 400, 500]

def reverse(l:list)->list:
    reversed_list = []
    for i in range(1, len(l)+1):
        ele = l[-i]
        reversed_list.append(ele)

    return reversed_list

print("original list: ", list1)

r_list = reverse(list1)

print("reversed list: ", r_list)