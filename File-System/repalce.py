filename = "File-System\learning_python.txt"

with open(filename) as file_object:
    content = file_object.readlines()
    for line in content:
        print(line.replace('python', 'C').rstrip())


for line in content:
    print(line.replace('python', 'php').rstrip())
