import json

filename = "File-System/json/username.json"

username = input("What's your name? ")
with open(filename, "w") as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
