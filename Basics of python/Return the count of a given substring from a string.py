string = "Emma is good developer. Emma is a writer"
sub_string = "is"
count = 0
i = 0

while i <= (len(string)-2):
    if sub_string == string[i:i+len(sub_string)]:
        count += 1
        i = i + len(sub_string)
    else:
        i += 1

print("Count: ", count)
