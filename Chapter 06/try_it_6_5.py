rivers = {
    "nile" : "egypt",
    "mississippi" : "united states",
    "euphrates" : "turkey"
}
for river, country in rivers.items():
    print(f"The {river.title()} river runs through the country of {country.title()}.")

print(f"\nRivers: ")

for river in rivers.keys():
    print(river.title())

print(f"\nCountries: ")

for country in rivers.values():
    print(country.title())