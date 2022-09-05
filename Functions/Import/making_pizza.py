# import pizza

# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# importing specific function

from pizza import make_pizza as mp
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# USING ALIAS
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
