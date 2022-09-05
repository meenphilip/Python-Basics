def collatz(number):
    while number != 1:
        print(number)
        if number & 1:
            number = 3 * number + 1
        else:
            number = number // 2
    return number


number = int(input("Enter a number: "))
result = collatz(number)
print(result)
