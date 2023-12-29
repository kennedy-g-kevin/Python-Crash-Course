def describe_city(city_name, country_name='United State of America'):
    """This function takes your input and writes a sentence with it."""
    print(f"{city_name.title()} is in {country_name.title()}")


describe_city('Los Angeles')
describe_city('Tokyo', 'Japan')
describe_city('Ontario', 'Canada')
