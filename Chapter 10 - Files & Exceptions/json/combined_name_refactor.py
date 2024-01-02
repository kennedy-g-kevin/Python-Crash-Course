import json

def get_stored_name():
    """Get stored name if available"""
    filename = 'name_of_user.json'
    # Try to open the file, if it exists, load the user's name.
    try:
        with open(filename) as f:
            username = json.load(f)
    # If file doesn't exist, do nothing.
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_name():
    username = input("What is your first and last name? ")
    first_name = username.split()[0]
    filename = 'name_of_user.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return first_name


def greet_user():
    """Greet the user by name"""
    username = get_stored_name()
    if username:
        first_name = username.split()[0]
        print(f"Welcome back, {first_name}!")
    else:
        first_name = get_new_name()
        print(f"We'll remember you when you come back, {first_name}!")


greet_user()
