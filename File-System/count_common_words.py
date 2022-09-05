def count_common_words(filename):
    """A program tha count common words in a file"""
    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError as e:
        # pass
        print(f"Error \n {e}")
    else:
        common_words = content.lower()
        count_words = common_words.count("dog")
        print(f"common words in {filename}  {count_words}")


filenames = ["File-System/cats.txt", "File-System/dogs.txt"]
for filename in filenames:
    count_common_words(filename)
