def count(str1:str, str2:str):
    count = str1.lower().count(str2.lower())
    print("count of ",str2,": ",count)

count("Welcome to USA. usa awesome, isn't it?", "USA")