import json

filename = 'name_of_user.json'

with open(filename) as f:
    username = json.load(f)
    first_name = username.split()[0]
    last_name = username.split()[1]
    print(f"Welcome back, {first_name}!")