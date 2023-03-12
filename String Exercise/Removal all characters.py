str1 = 'I am 25 years and 10 months old'
d_str = ""

for i in str1:
    if i.isdigit():
        d_str = d_str + i
    
print(d_str)