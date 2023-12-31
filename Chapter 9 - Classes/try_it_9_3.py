# Define a class called User. No () needed since it's being created from scratch.
class User:
    """Create a model for a user"""

    # Notes:
    # 1. Runs automatically at the time of an instance's creation. Needs to have two underscores before
    # and after. This helps distinguish it from native methods. It also ensure the method is called
    # automatically at instantiation of an instance.
    # 2. 'self' is required in the method definition and must be first. It refers to the instance itself
    # and it gives the individual instance access to the attributes and methods in the class.
    def __init__(self, first_name, last_name, username, date_of_birth):
        """Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.date_of_birth = date_of_birth

    def describe_user(self):
        """Describe user based on attributes"""
        print(f"{self.first_name.title()} {self.last_name.title()} goes by the handle of "
              f"{self.username} and was born on {self.date_of_birth}.")

    def greet_user(self):
        """Greet user using attributes."""
        print(f"Hi, {self.first_name.title()}!")


# Create instances of the defined class
me = User('kevin', 'k', 'user843845', '01/01/1900')
you = User('john', 'smith', 'jsmith1234', '01/02/1934')

# Call methods of a given class instance
me.describe_user()
me.greet_user()

you.describe_user()
you.greet_user()