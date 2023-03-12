def count(string: str):
    C_count = 0
    S_count = 0
    d_count = 0

    for i in string:
        if i.isalpha():
            C_count += 1
        elif i.isdigit():
            d_count += 1
        else:
            S_count += 1

    print("Digits: ",d_count)
    print("Characters: ",C_count)
    print("Symbols: ", S_count)

count("P@yn2at&#i5ve")
