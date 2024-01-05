class Car:
    """Attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given (argument) value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the argument amount to odometer"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't add negative miles!")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

# access attribute directly through an instance using dot notation
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# Take in new mileage via a method.
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

# Increment mileage by a number using a method
# Set initial reading at 23,500 and add 100 to it
my_new_car.update_odometer(23_500)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

# Don't allow negative miles to be added
my_new_car.increment_odometer(-100)
my_new_car.read_odometer()
