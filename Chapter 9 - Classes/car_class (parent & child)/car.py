"""Classes that can be used to represent gas and electric cars."""


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


class Battery:
    """Represents a battery for electric car class"""
    def __init__(self, battery_size=75):
        """Initialize battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print statement about the range of a battery."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Child class of car representing an electric car"""

    def __init__(self, make, model, year):
        """Initialize attributes of parent class"""
        super().__init__(make, model, year)
        # Initialize attributes particular to an electric car. self.battery points to Battery class.
        # calling the self.battery attribute gives us access to the methods and attributes of Battery class.
        self.battery = Battery()


    def fill_gas_tank(self):
        """Electric cars don't need gas tanks"""
        print("This car doesn't need gas")
