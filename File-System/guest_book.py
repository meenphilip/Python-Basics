filename = "File-System\guest_book.txt"

print("Enter 'quit' when you are finished.")
while True:
    name = input("What's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, "a") as file_object:
            file_object.write(name+"\n")
        print("Hi " + name + ", you've been added to the guest book.")
