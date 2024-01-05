# Define a class called User. No () needed since it's being created from scratch.
class User:
    """Create a model for a user"""


    def __init__(self, first_name, last_name, username, date_of_birth):
        """Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.date_of_birth = date_of_birth
        self.login_attempts = 0

    def describe_user(self):
        """Describe user based on attributes"""
        print(f"{self.first_name.title()} {self.last_name.title()} goes by the handle of "
              f"{self.username} and was born on {self.date_of_birth}.")

    def greet_user(self):
        """Greet user using attributes."""
        print(f"Hi, {self.first_name.title()}!")

    def increment_login_attempts(self):
        """Increment login attempts by one."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset number of login attempts"""
        self.login_attempts = 0



# Create instances of the defined class
me = User('kevin', 'k', 'user843845', '01/01/1900')
you = User('john', 'smith', 'jsmith1234', '01/02/1934')


# Increment login attempts from 0 to 3, then reset to 0
print(me.login_attempts)
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
print(me.login_attempts)
me.reset_login_attempts()
print(me.login_attempts)
