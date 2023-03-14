list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

def iterate(l1:list, l2:list2)->list:
    for x, y in zip(l1, l2[::-1]):
        print(x,y)

print("Lists: ",list1,"&", list2)
print("After iteration: ")
iterate(list1, list2)