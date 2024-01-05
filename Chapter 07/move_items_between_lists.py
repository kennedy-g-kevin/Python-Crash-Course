# create a list and set values equal to users who've not been confirmed
unconfirmed_users = ['alice', 'brian', 'candice']
# create empty list to store users after they've been confirmed
confirmed_users = []

# create while loop that continues until no values exist in unconfirmed
# users list
while unconfirmed_users:
    # create variable and set it equal to a user in the unconfirmed
    # users list while simultaneously removing the value from the list
    current_user = unconfirmed_users.pop()

    # print a statement for each user in the unconfirmed list
    print(f"Verifying user: {current_user.title()}")
    # add unconfirmed user to confirmed list
    confirmed_users.append(current_user)

# print a simple statement to screen
print(f"\nThe following users have been confirmed:")
# iterate through each user in the confirmed user list and print them.
for confirmed_user in confirmed_users:
    print(confirmed_user.title())