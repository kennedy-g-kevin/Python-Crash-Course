# create two lists; one of current users and one of users that would like to be
# added.
current_users = ['Ippsec', 'Jhammond', 'Jsmith34', 'Flipswxtch', 'Dedler16']
new_users = ['bwhite3', 'nocturne', 'Flipswxtch', 'github']

# create empty list. Iterate through current_users list to convert all iterations
# to lowercase
current_users_lowercase = [] 
for current_user in current_users:
    lowercase_username = current_user.lower()
    current_users_lowercase.append(lowercase_username)

# check each username in new_user to see if it is available for use.
for new_user in new_users:
    if new_user.lower() in current_users_lowercase:
        print(f"{new_user} is unavailable, please choose a different username.")
    if new_user.lower() not in current_users_lowercase:
        print(f"The username, {new_user}, is available for use!")