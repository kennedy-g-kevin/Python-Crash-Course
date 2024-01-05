class Restaurant:
    """An attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints description of a restaurant"""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Opens a restaurant"""
        print(f"{self.restaurant_name} is now open.")


my_restaurant_1 = Restaurant('Meowzers', 'Italian')
my_restaurant_2 = Restaurant('Arrgh', 'Pirate')
my_restaurant_3 = Restaurant('Woof', 'Dog')

my_restaurant_1.describe_restaurant()
my_restaurant_2.describe_restaurant()
my_restaurant_3.describe_restaurant()
