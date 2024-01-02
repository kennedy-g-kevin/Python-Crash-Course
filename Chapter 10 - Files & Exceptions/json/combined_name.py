import json

filename = 'name_of_user.json'

# Try to open the file, if it exists, load the user's name.
try:
    with open(filename) as f:
        username = json.load(f)
        first_name = username.split()[0]

# If file doesn't exist, prompt for a first and last name. Save it to file and print a message.
except FileNotFoundError:
    username = input("What is your first and last name? ")
    first_name = username.split()[0]
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {first_name}!")

# If the file does exist, welcome the user back.
else:
    print(f"Welcome back, {first_name}!")
