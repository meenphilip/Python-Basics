requested_toppings = ['mushroom', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we\'re out of the green peppers right now! ')
    else:
        print(f"Adding {requested_topping}")
        
print('\nFinished making your pizza!')
