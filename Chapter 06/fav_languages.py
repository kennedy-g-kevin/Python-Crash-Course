favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

# language = favorite_languages['sarah']
# print(f"Sarah's favorite programming language is {language}.\n")

# ask user to enter their first name, store as variable named user
user = input("To see if you are in our records, please enter your "
    "first name: ").lower()

# check favorite languages dictionary to see if the user name is listed. If it 
# is listed, print hello to the user and their favorite language
if user in favorite_languages.keys():
    record_statement = "According to our records, your favorite programming "
    "language is"
    print(f"Hello {user.title()}!")
    print(f"{record_statement} {favorite_languages[user]}.")

# if the user is not in the dictionary, ask if they would like to be added.
elif user not in favorite_languages.keys():
    print("We do not have a record for you on file.")
    add_user = input("Would you like to be added? Y/N: ")
    
    # if they would like to be added, prompt the user for their first name and
    # their favorite language. Add both items to the dictionary
    if add_user.lower() == 'y':
        new_user = input("Please provide your first name: ").lower()
        new_language = input("Please provide your favorite programming "
            "language: ").lower()
        favorite_languages[new_user] = new_language
        print(f"Thank you {new_user.title()}. We have added "
            "{new_language.title()} to our records as your favorite "
                "programming language!")
    
    # if the user does not want to be added, print a simple statement
    elif add_user.lower() == 'n':
        print(f"No problem, {user.title()}. You will not be added. "
            "Have a good day!")

print(f"\n{favorite_languages}")