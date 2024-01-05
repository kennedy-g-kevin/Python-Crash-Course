people = {
    'kevin' : {
        'first_name' : 'kevin',
        'last_name' : 'kennedy',
        'age' : '31',
        'city' : 'columbus',
    },
    
    'ben' : {
        'first_name' : 'ben',
        'last_name' : 'aune',
        'age' : '30',
        'city' : 'columbus'
    },

    'ryen' : {
        'first_name' : 'ryen',
        'last_name' : 'aune',
        'age' : '32',
        'city' : 'columbus'
    },

    'mom' : {
        'first_name' : 'barb',
        'last_name' : 'kennedy',
        'age' : 'unknown',
        'city' : 'mount vernon'
    }
} 

for person, person_info in people.items():
    full_name = f"{person_info['first_name'].title()} {person_info['last_name']}"
    age = f"{person_info['age']}"
    city = f"{person_info['city']}"

    print(f"\nPerson: {person.title()}")
    print(f"Age: {age.title()}\nCity: {city.title()}")