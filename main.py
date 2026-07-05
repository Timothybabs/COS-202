print("====== MATHEMATICAL CALCULATOR ======")

while True:
    print("\nChoose an operation:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("^  Power")
    print("%  Modulus")
    print("C  Clear")
    print("OFF Exit")

    choice = input("Enter your choice: ").upper()

    if choice == "OFF":
        print("Calculator Closed.")
        break

    if choice == "C":
        print("\n" * 20)
        continue

    if choice in ["+", "-", "*", "/", "^", "%"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "+":
            print("Answer =", num1 + num2)
        elif choice == "-":
            print("Answer =", num1 - num2)
        elif choice == "*":
            print("Answer =", num1 * num2)
        elif choice == "/":
            if num2 != 0:
                print("Answer =", num1 / num2)
            else:
                print("Division by zero is not allowed.")
        elif choice == "^":
            print("Answer =", num1 ** num2)
        elif choice == "%":
            print("Answer =", num1 % num2)
    else:
        print("Invalid choice.")