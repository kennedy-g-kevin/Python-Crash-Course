pizza = {
    'crust' : 'thin',
    'toppings' : ['pepperoni', 'sausage', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")