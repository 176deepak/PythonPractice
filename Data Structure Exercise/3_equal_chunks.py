sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

def chunks(l: list) -> list:
    cSize = len(l)//3
    start = 0
    end = cSize

    for i in range(3):
        index = slice(start, end)

        chunk = l[index]
        print(i+1,"chunk: ", chunk)
        print("After reversing: ", list(reversed(chunk)))

        start = end
        end += cSize

chunks(sample_list)