"""
Write a Python program that prints the first and last three characters of the string s as a single string.

If the string has less than six characters, print an empty string (blank output).
"""

str = "JavaScript"

num_chars = 3
if len(str) < num_chars * 2:
    pass
else:
    new_str = str[:num_chars] + str[len(str)-num_chars:]
    print(new_str)
