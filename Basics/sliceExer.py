sports = ["football", "Tennis", "BasketBall", "netBall", "NfL"]
# print("The first items in the lista are:\n")
# for sport in sports[:3]:
#     print(sport)


# print("The midlle items in the lista are:\n")
# print(sports[1:3])

# print("The last 3 items in the list are:\n")
# lastThree = sports[1:]
# print(lastThree)

myPizza = ["Pepporoni", "chicken", "falafel", "Pilau", "carrots"]
friendPizza = myPizza[:]
myPizza.append("Cheese")
# print(myPizza)
friendPizza.append("Nyama Choma")
# print(friendPizza)
print("My Favourite pizzas are:")
for pizza in myPizza:
    print(pizza)


print("\nMy friend Favourite pizzas are:")
for fpizza in friendPizza:
    print(fpizza)
