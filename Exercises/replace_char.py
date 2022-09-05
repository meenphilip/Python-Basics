"""
Write a Python program that prints the string s with the character curr_char replaced by the character new_char.

curr_char and new_char are variables that contain strings with a single character.

You may assume that new_char will not be an empty string.

The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).

If no match is found, print the initial string.
"""

# option 1
str = "hello"

curr_char = "l"
new_char = "s"

replaced_str = str.replace(curr_char, new_char)
print(replaced_str)

# option 2
s = "python"
new_ch = ""

cur_char = "p"
new_s = "x"

for char in s:
    if char == cur_char:
        new_s += new_ch
    else:
        new_s += char
print(new_s)
