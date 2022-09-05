favourite_place = {
    'sean': ['new york', 'nairobi'],
    'brian': ['nakuru', 'kitale', 'kisumu'],
    'justin': ['boston', 'juba'],
    'hafsa': ['liverpool']
}
# loop
for person, places in favourite_place.items():
    if len(places) == 1:
        print("\n" + person.title()+" Here is your favourite place:")
        for place in places:
            print(place.title())
    else:
        print("\n" + person.title()+" Here are your favourite places:")
        for place in places:
            print(place.title())
