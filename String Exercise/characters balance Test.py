def balance(str1:str, str2:str) -> str:
    flag = True

    for i in str1:
        if i not in str2:
            flag = False
            return flag
    
    return flag

res = balance("Ynf", "PYnative")

print(res)