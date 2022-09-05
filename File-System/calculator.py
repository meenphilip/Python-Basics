prompt = "Enter two numbers to be added"
prompt += "\nEnter 'q' to quit the programe"
print(prompt)

while True:
    try:
        first_num = int(input("\nEnter first number please: "))
        if first_num == "q":
            break

        second_num = int(input("Enter second number please: "))
        if second_num == "q":
            break

    except ValueError:
        print("Sorry numbers only!")
        break
    else:
        sum = first_num + second_num
        print(sum)
