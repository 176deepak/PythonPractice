str1 = "Emma is a data scientist who knows Python. Emma works at google."
word = "Emma"

def lastPosition(str1: str, str2: str) -> int:
    index = str1.rfind(str2)
    return index

res = lastPosition(str1, word)
print("Last position: ", res)