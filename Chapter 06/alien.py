# create dictionary, create two keys with associated values
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# create empty dictionary to add keys and values to it
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(f"\n{alien_0}")

# change color value to yellow
alien_0['color'] = 'yellow'
print(alien_0)

# make x position value increase through value of speed key
alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print(f"Alien's original x position: {alien_0['x_position']}")

# update value of speed key to fast
alien_0['speed'] = 'fast'

# look at value of speed key and determine x coordinate change based on it
if alien_0['speed'] == 'slow':
    x_position_change = 1
elif alien_0['speed'] == 'medium':
    x_position_change = 2
else:
    x_position_change = 3

# modify x position value by adding the value from the above if/elif/else statement
alien_0['x_position'] = alien_0['x_position'] + x_position_change
print(f"Alien's new x position: {alien_0['x_position']}")

