pokemon_versions = ['red', 'blue', 'yellow', 'black 2']


print("\n", pokemon_versions)

my_first_version = pokemon_versions.pop(0)
my_last_version = pokemon_versions.pop(-1)
brother_owned_version = 'blue'
pokemon_versions.remove(brother_owned_version)

print(f"The first version of Pokemon that I owned was {my_first_version.title()}, and the last version that I owned was {my_last_version.title()}.")
print(f"I did not play {brother_owned_version} since my brother owned it; I felt as though it was his and his alone.")
print(pokemon_versions, "\n")