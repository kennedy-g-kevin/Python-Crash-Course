# create a variable called prompt and set its value to a string
prompt = "\nTell me something, and I will repeat it back to you:"
# concatenate another string to the prompt variable
prompt += "\nEnter 'quit' to end the program. "
# create variable for while loop, its value is false
user_wants_exit = False

# create while loop that starts based on the value of the variable created
while user_wants_exit == False:
    # user prompt variable to ask for and store user input
    ask_user_input = input(prompt)

    # make a decision based on the user's input
    if ask_user_input != 'quit':
        user_wants_exit = False
        print(ask_user_input)
    elif ask_user_input == 'quit':
        break