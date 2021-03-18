who_id_invite = ['grandma', 'Ben', 'Ryen']

print(f"I miss you {who_id_invite[0].title()}, would you like to go get dinner?")
print(f"Hello, {who_id_invite[1].title()} and {who_id_invite[-1].title()}. Do you guys want to get dinner tonight?")

print(f"{who_id_invite[-1].title()} can't make it.")

who_id_invite[-1] = 'dustin'

print(f"I asked {who_id_invite[-1].title()} if he wanted to come along instead.")
print('\n\n\n')
print("I was able to find a bigger table so more people can be invited!")

who_id_invite.insert(0, 'tim')
who_id_invite.insert(0, 'mom')
who_id_invite.append('dad')
print(f"I've decided to invite {who_id_invite[0].title()}, {who_id_invite[1].title()}, and {who_id_invite[-1].title()} to the dinner as well.\n\n")

for guest in who_id_invite:
    print(f"This is an invitation to {guest.title()} for dinner tonight")

print(f"I am inviting {len(who_id_invite)} people to dinner")