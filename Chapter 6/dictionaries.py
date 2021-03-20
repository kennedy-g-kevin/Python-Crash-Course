# create dictionary
kevin = {'height' : "6'1", 'weight' : '160 lbs'}

# print both key's values
print(f"Kevin's height is {kevin['height']} and his weight is {kevin['weight']}.")

# create another dictionary and print values
kevin_two = {'shoe_size' : 12, 'shirt_size' : 'medium'}
print(f"Kevin's shoe size is {kevin_two['shoe_size']} and his shirt size is {kevin_two['shirt_size']}.")

# create third dictionary and print values
kevin_three = {'primary_color' : 'black', 'secondary_color' : 'red', 'fav_food' : 'pasta'}
print(f"Kevin's favorite color combination is {kevin_three['secondary_color']} on {kevin_three['primary_color']} and his favorite food is {kevin_three['fav_food']}.\n")

# add new key-value pairs to dictionary three
kevin_three['car'] = 'honda civic si'
kevin_three['fav_game'] = 'final fantasy vii'

# print value of car key and print entire dictionary to see changes made above
print(kevin_three['car'].title())
print(f"\n{kevin_three}")