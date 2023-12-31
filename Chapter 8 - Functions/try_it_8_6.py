def city_country(city_name, country_name):
    """This function takes input and returns output"""
    return f"{city_name.title()}, {country_name.title()}"


call_1 = city_country('Los Angeles', 'United State of America')
call_2 = city_country('Tokyo', 'Japan')
call_3 = city_country('Ontario', 'Canada')

print(call_1)
print(call_2)
print(call_3)
