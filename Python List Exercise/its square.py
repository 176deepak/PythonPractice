numbers = [1, 2, 3, 4, 5, 6, 7]
print("List: ", numbers)

def square(l:list)->list:
    for i in range(len(l)):
        l[i] = l[i]**2
    return l

squres = square(numbers)
print("Squared list: ",squres)