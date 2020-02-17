alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']

print(alien_0['color'])
print(alien_0['points'])

print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

cat = {}

cat['name'] = 'Anna'
cat['age'] = 5

print(cat)

del cat['age']

print(cat)

# point_value = cat['points'] # KeyError
point_value = cat.get('points', 'No point value assigned.')
print(point_value)

user_0 = {
    'username': 'hwebz',
    'first': 'Ha',
    'last': 'Manh Do',
    'age': 'Ha',
    'address': 'Manh Do'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for key in user_0.keys():
    print(f"Key: {key}")

if 'age' not in user_0.keys():
    print('Age is not defined')

for key in sorted(user_0.keys()):
    print(f"Key: {key}")

for value in user_0.values():
    print(f"Value: {value}")

for value in set(user_0.values()):
    print(f"Unique value: {value}")

# building a set
languages = {'python', 'ruby', 'python', 'c'}
print(languages)

alien_1 = {'color': 'green', 'points': 5}
alien_2 = {'color': 'yellow', 'points': 10}
alien_3 = {'color': 'red', 'points': 15}

aliens = [alien_1, alien_2, alien_3]

for alien in aliens:
    print(alien)

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'low'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show first 5 aliens
for alien in aliens[:5]:
    print(alien)

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:'")
    for language in languages:
        print(f"\t{language.title()}")


users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")