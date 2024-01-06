"""Test for employee info class"""
import unittest
from employee_info import Employee


class TestEmployeeInfo(unittest.TestCase):
    """Create test case."""

    def setUp(self):
        """Set up other methods"""
        self.my_employee = Employee('Kevin', 'Kennedy', 50_000)

    def test_give_default_raise(self):
        """Test for giving a default raise"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 55_000)

    def test_give_custom_raise(self):
        """Test a custom raise amount."""
        self.my_employee.give_raise(10_000)
        self.assertEqual(self.my_employee.annual_salary, 60_000)


if __name__ == '__main__':
    unittest.main()
