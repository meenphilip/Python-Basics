filename = "File-System\guest.txt"

name = input("What's your name: ")
with open(filename, 'w') as file_object:
    file_object.write(name)
