sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

new_dict={}

for key in keys:
    if key in sample_dict:
        new_dict[key] = sample_dict[key]

print("New dict: ", new_dict)