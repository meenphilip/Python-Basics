filename = "File-System/own_file.txt"

prompt = "Enter 'q' to exit the programme"
while True:
    reason = input("Why programming? ")
    if reason == "q":
        break

    with open(filename, 'a') as f:
        f.write(reason + "\n")
    print("Your reason :" + reason)
