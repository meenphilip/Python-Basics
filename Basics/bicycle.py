bicycles = ['trek', 'cannondales', 'redline', 'specialized']
# print(bicycles)
# Accessing Elements in a List

# print(bicycles[-1].title())
# EXe 1
names = ['Philip', 'Meen', 'Tycoon']
# print(names[0].lower())
# print(names[1].upper())
# print(names[2].title())

# EXe 2

msg = "Timo calls " + names[0] + " instead of "+names[2]
# print(msg)

# EXe 3
transportation = ["Car", "bicycle", "train", "Air"]
dream = "i would like to own "+transportation[0] + "of type BMW"
# print(dream)

motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles[0] = 'ducati'
motorcycles.append('meen')
insertItems = ["justo", "baro", "Yen"]
motorcycles.insert(3, insertItems)
# print(motorcycles)

cars = ['bMW', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
print("Sorted func\n"+str(sorted(cars)))
print(cars)
