import json

username = input("What is your first and last name? ")
first_name = username.split()[0]

filename = 'name_of_user.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {first_name}!")
