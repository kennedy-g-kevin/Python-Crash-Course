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

    def fill_gas_tank(self, gallons):
        print(f"This car takes {gallons} gallons of gas!")


class ElectricCar(Car):
    """Child class of car representing an electric car"""

    def __init__(self, make, model, year):
        """Initialize attributes of parent class"""
        super().__init__(make, model, year)
        # Initialize attributes particular to an electric car
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't need gas tanks"""
        print("This car doesn't need gas")


my_civic = Car('honda', 'civic', 2019)
my_tesla = ElectricCar('testa', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_civic.fill_gas_tank(16)
my_tesla.fill_gas_tank()
