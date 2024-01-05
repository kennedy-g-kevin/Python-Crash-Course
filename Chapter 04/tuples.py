# tuples are immutable lists; the values containted inside of them can not be changed!

foods_offered = ('pizza', 'wings', 'sandwiches', 'pasta', 'dessert')
# foods_offered[1] = 'python'        # this does not work when ran

print("This is the original menu:")
for food in foods_offered:
    print(food)


print()
print("This is the updated menu:")
foods_offered = ('pizza', 'wings', 'sandwiches', 'pasta', 'dessert', 'alligator', 'squirrel')
for food in foods_offered:
    print(food)