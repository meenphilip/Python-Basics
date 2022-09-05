motorcycles = ['honda', 'yamaha', 'suzuki']
# modifying list elements
motorcycles[0] = 'dollar'
# print(motorcycles)

# adding an item to the end of a list
# use append()
# added = ['granada', 'ducati']
motorcycles.append('ducati')
# print(motorcycles)

# Inserting Elements into a List

motorcycles.insert(4, 'granada')
# print(motorcycles)

# Removing Elements from a List

# Using del
del motorcycles[0]
# print(motorcycles)

# popped_motorcycles = motorcycles.pop()
# print(popped_motorcycles)
# print(motorcycles)

# Popping Items from any Position in a List
first_owned = motorcycles.pop(0)
# print('The first motorcycle I owned was a ' + first_owned.title())

# Removing an Item by Value
# Remove()
# motorcycles.remove('suzuki')
# print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

