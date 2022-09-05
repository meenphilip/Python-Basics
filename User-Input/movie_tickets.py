prompt = "\nPlease enter your: "
active = True
while active:
    age = int(input(prompt))

    if age <= 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    print("Your price ticket is $" + str(price))
