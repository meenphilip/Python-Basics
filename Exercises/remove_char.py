"""
Write a Python program that prints the string s without the characters located at even indices.

If the string is empty or only has one character, print it intact.
"""
str = "python"
new_str = ""

for i in range(len(str)):
    if i % 2 != 0:
        new_str += str[i]

print(new_str)

# second implimentation
for i in range(1, len(str), 2):
    new_str += str[i]
print(new_str)
