cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print('False')
elif age_0 >= 21 and age_1 >= 18:
    print('Wow!!!')
else:
    print('True')

if 'bmw' in cars:
    print('BMW is there! Wow!')

if 'mazda' not in cars:
    print('Mazda not in there!')

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping:
    print('Adding mushrooms.')
elif 'peperoni' in requested_toppings:
    print('Adding peperoni.')
elif 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('Finished making your pizza')

toppings = []

if toppings:
    for topping in toppings:
        print(f"Adding {topping}")
    print(f"Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

a_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
r_toppings = ['mushrooms', 'french fries', 'extra cheese']

for r_topping in r_toppings:
    if r_topping in a_toppings:
        print(f"Adding {r_topping}")
    else:
        print(f"Sorry, we don't have {r_topping}")
print("Finished making your pizza")