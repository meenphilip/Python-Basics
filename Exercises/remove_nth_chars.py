"""
Write a Python program that prints the string s without the character at index n.

If the index n is out of range, print the string s intact.

If the string s is empty, print the string s intact.
"""
str = "Hello"
n = 1

# if (len(str) == 0 or (n >= len(str))):
if(not str or (n >= len(str))):
    print(str)
else:
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
    print(new_str)
