# create a dictionary
glossary = {
    'variable' : 'named space in memory for data',
    'tuple' : 'immutable list',
    'dictionary' : 'container for key-value pairs that can hold any amount of information',
    'title' : 'method that capitalizes the first letter of a word',
    'sorted' : 'method that sorts data passed to it; ie, list, dictionary',
}

# add three key-value pairs to dictionary
glossary['print'] ='function that prints chosen characters, variables, or other output to screen'
glossary['slice'] = 'tool that allows a user to perform work on specifically selected items in a list'
glossary['operands'] = """symbols that are used to set values equal to one another, \
check if values are equal to each other, and other things."""

# loop through all items in dictionary, print items
for term, definition in glossary.items():
    print(f"{term} : {definition}")