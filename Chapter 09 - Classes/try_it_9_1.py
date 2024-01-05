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


my_restaurant = Restaurant('Meowzers', 'Italian')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
