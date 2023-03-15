keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

def dic(l1:list, l2:list, size:int)->dict:
    dictionary = dict()
    for i in range(size):
        dictionary[l1[i]]=l2[i]
    
    return dictionary

dictionary=dic(keys,values,3)
print("Lists: ",keys,"&",values)
print("Dictionary: ", dictionary)