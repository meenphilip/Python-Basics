import json
filename = "username.json"
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError as e:
    username = input("What's your name? ")
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
        print("we'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
