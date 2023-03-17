tuple1 = (11, 22)
tuple2 = (99, 88)

temp = tuple1
tuple1 = tuple2
tuple2 = temp

print("After swapping: \ntuple1: ",tuple1,"\ntuple2: ",tuple2)