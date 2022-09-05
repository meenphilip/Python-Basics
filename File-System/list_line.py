"""
Making a List of Lines from a File.
Storing file content outside with block
"""

filename = ('File-System\pi_digits.txt')

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
