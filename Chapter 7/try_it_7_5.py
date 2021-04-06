user_continue = True

while user_continue == True:
    user_input = input("Type quit to exit or enter an attendants \
age: ")

    if user_input == 'quit':
        print("Thank you for using our system!")
        break
    else:
        user_age = int(user_input)
        if user_age < 3:
            cost = 'free'
        elif user_age >= 3 and user_age <= 12:
            cost = '10$'
        elif user_age > 12:
            cost = '15$'
    print(f"The cost for someone the age of {user_age} is {cost}.\n")