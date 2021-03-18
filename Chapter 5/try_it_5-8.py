usernames = ['admin', 'flipswxtch', 'nocturne', 'glymere', 'dedler16']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello superuser, what administrative tasks are to be done today?")
        else:
            print(f"Hello, {username.title()}. Thank you for logging in today.")
else:
    print("We need to get some usernames!")
    print()