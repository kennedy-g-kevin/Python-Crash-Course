class Restaurant:
    """An attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 2

    def describe_restaurant(self):
        """Prints description of a restaurant"""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Opens a restaurant"""
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, number):
        """Sets the number of customers served"""
        self.number_served = number

    def increment_number_served(self, number):
        """Add to number served based on argument provided."""
        self.number_served += number
        print(f"A total of {self.number_served} customers were served today`")


class IceCreamStand(Restaurant):
    """Model of an ice cream stand; a child class of Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes from parent class"""
        super().__init__(restaurant_name, cuisine_type)
        """Initialize attributes specific to ice cream stand"""
        self.flavors = ['chocolate', 'vanilla', 'mint chocolate chip']
        print(f"{self.restaurant_name.title()} currently offers the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


my_restaurant = Restaurant('Meowzers', 'Italian')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print()
ice_cream_stand = IceCreamStand("Kel's Ice Cream", 'dessert')