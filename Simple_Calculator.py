# Simple Calculator with Proper Loop

print("---- Simple Calculator ----")
print("Operations: +  -  *  /")

while True:
    num1 = float(input("\nEnter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print("Result:", num1 + num2)

    elif op == "-":
        print("Result:", num1 - num2)

    elif op == "*":
        print("Result:", num1 * num2)

    elif op == "/":
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("Result:", num1 / num2)

    else:
        print("Invalid operator! Please choose +, -, *, /")

    # Ask user again until valid input
    while True:
        choice = input("\nDo you want to calculate again? (yes/no): ").lower()

        if choice == "yes":
            break   # continue main loop

        elif choice == "no":
            print("Calculator closed. Goodbye!")
            exit()

        else:
            print("Invalid input! Please type 'yes' or 'no'.")