filename = "File-System\polling.txt"

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break


with open(filename, "a") as file_object:
    for response in responses:
        file_object.write(response + "\n")
