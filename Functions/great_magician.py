def make_great(names, great):
    while names:
        new_name = names.pop()
        print("Modifying :" + new_name)
        great.append(new_name)


def show_magicians(names):
    print("\nThe following names have been modified:")
    for name in names:
        msg = "The Great, " + name.title() + "!"
        print(msg)


magicians = ['Harry hudinn', 'tom', 'jerry']
great = []
# calling make_great with list and new list
make_great(magicians[:], great)
# call with new great[]
show_magicians(great)
