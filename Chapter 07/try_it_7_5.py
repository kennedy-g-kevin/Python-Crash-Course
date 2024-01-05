# create variable and set the value as true
user_continue = True

# create while loop that starts cause user_continue is true
while user_continue == True:
    # create variable that takes user input
    user_input = input("Type quit to exit or enter an attendants \
age: ")

    # if user input is quit, exit the while loop
    if user_input == 'quit':
        print("Thank you for using our system!")
        break
    # if user input isn't quit, print to screen based upon number provided by
    # the user. the program will then reprompt for input
    else:
        user_age = int(user_input)
        if user_age < 3:
            cost = 'free'
        elif user_age >= 3 and user_age <= 12:
            cost = '10$'
        elif user_age > 12:
            cost = '15$'
    print(f"The cost for someone the age of {user_age} is {cost}.\n")