def read_files(filename):
    """A program that read to differnt files"""
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        # Error report mode
        print("Sorry file not found!")
        # Error silent mode
        # pass
    else:
        print(content)


# need to iterated to work
filename = ["File-System/cats.txt", "File-System/dogs.txt"]
for file in filename:
    read_files(file)
