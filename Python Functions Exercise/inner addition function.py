def outer(a, b):
    def inner():
        return a + b
    
    return inner() + 5

res = outer(10, 15)
print(res)