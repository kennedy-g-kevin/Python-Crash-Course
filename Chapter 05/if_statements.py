import random

age = 4

while age >= 4:
    age = random.randint(1,100)
    print(f"The person's age: {age}")
    if age < 4:
        if age == 1:
            print(f"Their entry is free since they are only {age} year old.")
        else:
            print(f"Your entry is free since you are {age} years old.")
    elif age < 18:
        print("Your cost of entry is $25.00")
    elif age >= 18:
        print("Your cost of entry is $40.00")
    print()