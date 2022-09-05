import json
# filename = "File-System/json/username.json"


# def greet_user(filename):
#     """Greet the user by name."""
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError as e:
#         username = input("What's your name? ")
#         with open(filename, "w") as f_obj:
#             json.dump(username, f_obj)
#             print("we'll remember you when you come back, " + username + "!")
#     else:
#         print("Welcome back, " + username + "!")


# greet_user(filename)


def get_stored_username():
    """Get stored username if available."""
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    filename = "username.json"
    username = input("What's your name? ")
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
        print("we'll remember you when you come back, " + username + "!")
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("we'll remember you when you come back, " + username + "!")


greet_user()
