def format_city_country(city_name, country_name, population=''):
    """Format a city and country name."""
    if population:
        formatted_city_country = f"{city_name}, {country_name} - population {population}"
    else:
        formatted_city_country = f"{city_name}, {country_name}"
    return formatted_city_country.title()
