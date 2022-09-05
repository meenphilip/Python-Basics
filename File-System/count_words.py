def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as file_object:
            content = file_object.read()

    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist!"
        print(msg)

    else:
        # Count the approximate number of words in the file.
        words = content.split()
        num_words = len(words)
        print("The file " + filename + " has about " +
              str(num_words) + " words.")


# file list directory
filename = ["File-System/alice.txt",
            "File-System/guest_book.txt", "learning_python.txt"]
for file in filename:
    count_words(file)
