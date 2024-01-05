# create a list and add pet type values to it
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print the pets list
print(pets)

# create while loop that continues while the value of cat is in the pets list
while 'cat' in pets:
    # remove each value of cat while iterating through the list
    pets.remove('cat')

# print the list and see no cat values exist anymore
print(pets)