prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
user_wants_exit = False

while user_wants_exit == False:
    ask_user_input = input(prompt)

    if ask_user_input != 'quit':
        user_wants_exit = False
        print(ask_user_input)
    elif ask_user_input == 'quit':
        break