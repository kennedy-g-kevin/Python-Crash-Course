pets = {
    'cedric' : {
        'type' : 'dog',
        'owner' : 'ryen',
    },
    
    'smokey' : {
        'type' : 'horse',
        'owner' : 'barb',
    },
    'copper' : {
        'type' : 'cat',
        'owner' : 'aimee',
    },
}

for pet, pet_info in pets.items():
    pet_type = f"{pet_info['type']}"
    pet_owner = f"{pet_info['owner']}"

    print(f"\n{pet.title()}")
    print(f"\tType: {pet_type.title()}\n\tOwner: {pet_owner.title()}")