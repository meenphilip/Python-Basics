import json
filename = "favourite_num.json"

try:
    with open(filename, "r") as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What's your favourite number? ")
    with open(filename, "w") as f:
        json.dump(number, f)
        print("Thanks, I'll remember that.")
else:
    print("Here is your favourite number: " + number)
