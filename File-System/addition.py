
prompt = "Please provide to numbers to be added"
print(prompt)

try:
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
except ValueError:
    print("Invalid operation")
else:
    sum = first_num + second_num
    print(sum)
