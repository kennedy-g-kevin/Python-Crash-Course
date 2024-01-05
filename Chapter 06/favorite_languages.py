# create dictionary
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

# use get method, I'm assuming there's more to this but unsure yet.
my_fav_language = favorite_languages.get('kevin', 'No favorite language assigned.')
print(f"{my_fav_language}\n\n")

# loop through all keys and values in dictionary, print keys and values in a statement
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite programming language is {language.title()}.")

print(f"{sorted(favorite_languages)}")