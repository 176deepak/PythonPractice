x = [4, 6, 8, 24, 12, 2]

def maxEle(x):
    max = 0
    for i in x:
        if i > max:
            max = i
        
    print("Largest element: ", max)

maxEle(x)