print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to end the progamme")

while True:
    first_number = input("\nEnter the first number: ")
    if first_number == "q":
        break

    second_number = input("Enter the second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError as e:
        print(f"Error You can't divide by 0! {e}")
    else:
        print(answer)
