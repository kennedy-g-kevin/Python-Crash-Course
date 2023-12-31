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



my_restaurant = Restaurant('Meowzers', 'Italian')

# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

restaurant = Restaurant('Arrgh', 'Pirate')
print(restaurant.number_served)
restaurant.set_number_served(6)
print(restaurant.number_served)
restaurant.increment_number_served(6)