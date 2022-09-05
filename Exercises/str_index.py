# a program to get string index
name = "meen"
index = 1

if not name:
# if len(name) == 0:
    print("The string is Empty!")
elif index < len(name):
    print(name[index])
else:
    print("Oops string index is out of Range!")
