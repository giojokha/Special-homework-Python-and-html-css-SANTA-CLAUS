def calculator():
    print("Hi Guest! Welcome To The Python Made Mathematical Calculator")
    num1 = int(input("Enter The First Number:"))
    operator = input("Input The Mathematical Operator (+, -, *, /): ")
    num2 = int(input("Enter The Second Number:"))

    result = 0

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Big Blunder: You Cant Divide by 0")
            return

    print("Equals: {result}")

# კალკულატორის გაშვება
calculator()