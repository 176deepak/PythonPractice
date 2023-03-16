set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

union_set = set1.union(set2)
intersect_set = set1.intersection(set2)
union_set.difference_update(intersect_set)
print(union_set)