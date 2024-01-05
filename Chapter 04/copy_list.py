cars = ['civic', 'escape', 'altima', 'wrx']
models = cars[:]

cars.append('3000gt')
cars.append('supra')
models.append('stealth')
print(cars)
print(models)
print(f"\nThe first three models I typed out are:\n {cars[0:3]}.")
print(f"\nThree items from the middle of the list are:\n {cars[1:-2]}.")
print(f"\nThe three models at the end of my list are:\n {cars[-3:]}.")
print()

def cars_to_screen():
    print("The items I have in my list of cars are:")
    for car in cars:
        print(car)
    print()

def models_to_screen():
    print("The items I have in my list of models are:")
    for model in models:
        print(model)

cars_to_screen()
models_to_screen()