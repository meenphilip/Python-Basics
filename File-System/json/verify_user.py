import json


def get_stored_user():
    """Get stored username if available."""
    filename = "verify_user.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError as e:
        return None
    else:
        return username


def get_new_user():
    """Prompt for a new username."""
    username = input("What's your username? ")
    filename = "verify_user.json"
    with open(filename, "w") as f:
        json.dump(username, f)
        print("Thank you i'll remember that!")
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_user()
    if username:
        correct = input("Are you " + username + " ? (y/n): ")
        if correct == "y":
            print("Welcome back, " + username + " !")
        else:
            username = get_new_user()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_user()
        print("We'll remember you when you come back, " + username)


greet_user()
