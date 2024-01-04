import unittest
from city_functions import format_city_country


class CityCountryTest(unittest.TestCase):
    """Does a city like Santiago, Chile work?"""

    def test_city_country(self):
        formatted_city_country = format_city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_city_country = format_city_country('santiago', 'chile', '100000')
        self.assertEqual(formatted_city_country, 'Santiago, Chile - Population 100000')


if __name__ == '__main__':
    unittest.main()
