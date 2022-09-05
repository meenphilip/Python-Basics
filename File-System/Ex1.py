filename = "File-System\learning_python.txt"
"""print file content x3"""
# with open(filename) as file_object:
#     content = file_object.read()
#     print(content * 3)


"""print file content via a loop"""
# with open(filename) as file_object:
#     content = file_object.readlines()
#     for line in content:
#         print(line.rstrip())

"""print file content in a list"""
with open(filename) as file_object:
    lines = file_object.readlines()


for line in lines:
    print(line.strip())
