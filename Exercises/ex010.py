# Your Student ID: 240543604
# Your Name and Surname: Aylin-P-Saatlou

def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            operation = input("Enter operation (+, -, *, /): ").strip()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":

                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation! Please enter one of (+, -, *, /).")
                continue

            print(f"The result of {num1} {operation} {num2} = {result:.2f}")

        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        another_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if another_calculation != "yes":
            print("See you later!")
            break

calculator()
