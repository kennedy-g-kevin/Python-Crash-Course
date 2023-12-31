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


class Admin(User):
    """Model an admin user; child class of User"""

    def __init__(self, first_name, last_name, username, date_of_birth):
        """initialize attributes of parent class (User)"""
        super().__init__(first_name, last_name, username, date_of_birth)
        """initialize attributes particular to the admin class"""
        self.privileges = Privileges()


class Privileges:

    def __init__(self):
        """initialize attributes for the Privileges class"""
        self.privileges = ['create a user', 'delete a user', 'ban a user']

    def show_privileges(self):
        """Describes what the admin can do"""
        print(f"As an admin, I can perform the following functions:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Create instances of the defined class
me_an_admin = Admin('kevin', 'k', 'user843845', '01/01/1900')
me_an_admin.privileges.show_privileges()