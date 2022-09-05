prompt = "\nTell me something, I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

# intro of flags
active = True
message = ""
while message != "quit":
    message = input(prompt)

    if message != "quit":
        active = False
        print(message)
