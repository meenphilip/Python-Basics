import json

filename = "File-System/json/favourite_num.json"

# number = input("What's your favourite number? ")

# with open(filename, "w") as f_object:
#     json.dump(number, f_object)
#     print("Thanks! I'll remember that.")


with open(filename, "r") as f:
    content = json.load(f)
print("I know your favourite number is " + content)
