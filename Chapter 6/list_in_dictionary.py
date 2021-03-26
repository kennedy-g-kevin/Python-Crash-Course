pizza = {
    'crust' : 'thin',
    'toppings' : ['pepperoni', 'sausage', 'extra cheese']
}

# print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

# for topping in pizza['toppings']:
#     print(f"\t{topping}")

pizza = {
    'crusts' : ['thin', 'pan', 'hand tossed'],
    'toppings' : ['pepperoni', 'sausage', 'extra cheese']
}

for crust in pizza['crusts']:
    if crust == 'thin':
        print(f"You ordered a {crust} crust pizza with the following toppings: ")
    elif crust == 'pan' or crust == 'hand tossed':
        print(f"You ordered a {crust} pizza with the following toppings: ")
    for topping in pizza['toppings']:
        print(topping)
    print()

