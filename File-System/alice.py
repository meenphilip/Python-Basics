filename = "File-System/alice.txt"

try:
    with open(filename) as file_object:
        content = file_object.read()
        print(content)

except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist!"
    print(msg)

else:
    # Count the approximate number of words in the file.
    words = content.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
