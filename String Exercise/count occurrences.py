def count(string: str):
    string = string.lower()
    rec = {}

    for i in string:
        count = string.count(i)
        rec[i] = count

    print("Occurences: ", rec)

count("Apple")
