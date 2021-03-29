user_number = input("Select a number and I'll let you know if it's divisible \
by 10! ")

if int(user_number) % 10 == 0:
    print(f"The number {user_number} is divisible by ten.")
else:
    print(f"The number {user_number} is not divisible by ten.")