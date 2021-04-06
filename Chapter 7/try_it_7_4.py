user_continue = True

while user_continue == True:
    message = input("Enter a topping you would like added to your pizza: ")
    
    if message == 'quit':
        print(f"Thank you for creating a pizza, bye!")
        break
    else:
        print(f"Adding {message} to your pizza!\n")