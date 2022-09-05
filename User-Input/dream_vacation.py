dream_vacation = {}

active = True
while active:
    dream = input("\nWhat is you dream vacation? ")
    places = input(
        "If you could visit one place in the world,where would you go? ")

    dream_vacation[dream] = places

    repeat = input("Would you like to let another person response? (yes/no) ")
    if repeat == 'no':
        active = False

print("\n------ poll results ------")
for dream, places in dream_vacation.items():
    print(dream + " would be at " + places)
