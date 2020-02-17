def greet_user():
    """Display a simple greeting."""
    print("Hello!")

def greet_another_user(username):
    print(f"Hello, {username}")

def describe_pet(animal_type, pet_name='Katty'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

def get_formatted_name_2(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello,, {name.title()}"
        print(msg)

def print_models(unprinted_designs, completed_models):
    """ Simulate printing each design, until none are left.
        Move each design to completed_models after printing. """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_models(completed_models):
    """ Show all the models that were printed. """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    print(toppings)

def build_profile(first, last, **user_info):
    """ Build a dictionary containing everything we know about a user. """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

greet_user()
greet_another_user('Jeesie')
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(pet_name='katty', animal_type='cat')

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician_2 = get_formatted_name_2('jimi', 'hendrik', 'lee')
print(musician_2)

musician_3 = build_person('jimi', 'hendrix')
print(musician_3)

musician_4 = build_person('jimi', 'hendrix', 30)
print(musician_4)

# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     if f_name == 'quit':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'quit':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}")

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# pass by reference
# print_models(unprinted_designs, completed_models)
# pass by value
print_models(unprinted_designs[:], completed_models)
show_models(completed_models)

print(unprinted_designs)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)