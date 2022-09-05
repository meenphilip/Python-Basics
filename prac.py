# while True:
#     age = input("Enter age: \n")
#     if age.isdecimal():
#         print(age)
#         break

#     print("Please enter a number for age")


# while True:
#     password = input("Enter Password (numbers and letters only):\t")
#     if password.isalnum():
#         break
#     print('Password should be letter and numbers only')


def print_picnicItem(itemsDict, leftWidth, rightWidth):
    print("PICNIC ITEMS".center(leftWidth + rightWidth, "-"))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, ".") + str(v).rjust(rightWidth))


picnicItems = {
    "sandwich": 2,
    "applles": 12,
    "cups": 4,
    "cookies": 8000,
    "cup cakes": 4500,
    "bread": 89,
}

print_picnicItem(picnicItems, 12, 5)
print_picnicItem(picnicItems, 20, 6)
