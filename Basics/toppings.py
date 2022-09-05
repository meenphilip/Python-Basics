# requested_topping = 'mushroom'
# if requested_topping != 'Anchovies':
#     print('Hold the anchovies')

requested_toppings = ['mushroom', 'extra cheese']
if 'mushroom' in requested_toppings:
    print('Adding mushroom')
if 'pepperoni' not in requested_toppings:
    requested_toppings.append('pepperoni')
    print('Adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')

print('\nFinished making your pizza!')
print(requested_toppings)
