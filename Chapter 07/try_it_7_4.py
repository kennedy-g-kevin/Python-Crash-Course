# create variable for while loop and set the value to true
user_continue = True

# create while loop that continues as long as the above variable equals true
while user_continue == True:

    # create variable and set user input as its value
    message = input("Enter a topping you would like added to your pizza: ")
    
    # if the user input is quit, exit the while loop, otherwise the loop
    # continues
    if message == 'quit':
        print(f"Thank you for creating a pizza, bye!")
        user_continue = False
    else:
        print(f"Adding {message} to your pizza!\n")