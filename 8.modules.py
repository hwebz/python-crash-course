# import pizza
# from pizza import *
from pizza import make_pizza as mp, build_profile as bp

# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# user_profile = pizza.build_profile('albert', 'einstein', location='princeton', field='physics')
# print(user_profile)

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

user_profile = bp('albert', 'einstein', location='princeton', field='physics')
print(user_profile)