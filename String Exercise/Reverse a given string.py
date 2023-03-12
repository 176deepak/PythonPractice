def reverseStr(string: str) -> str:
    rev = string[: :-1]

    return rev

string = reverseStr("PYnative")
print("Reversed string: ", string)