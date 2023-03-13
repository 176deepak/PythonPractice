sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

def count(l: list) -> dict:
    rec = dict()
    for i in l:
        count = l.count(i)
        rec[i] = count

    return rec

res = count(sample_list)
print("counts: ", res)
