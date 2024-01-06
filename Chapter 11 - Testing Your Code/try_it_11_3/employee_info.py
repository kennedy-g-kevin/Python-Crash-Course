"""Class that looks to model an employee"""


class Employee:
    """Model an employee"""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5_000):
        self.annual_salary += amount
        return self.annual_salary

