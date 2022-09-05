import json

filename = "File-System/json/username.json"
with open(filename, "r") as f_obj:
    username = json.load(f_obj)

print("Welcome back, " + username + "!")
