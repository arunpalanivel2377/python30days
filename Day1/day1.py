"""
✅ Day 1: Calculator + Challenges + Concept Review
📌 1. Project: Command-Line Calculator
🔧 Features:
Ask the user to choose an operation: +, -, *, /

Take two numbers as input

Perform the operation and show the result

Allow user to run again or exit

🧠 Concepts: input(), float(), if-elif-else, while loop
"""

def addition(num1,num2):
    print(f"Addition: {num1 + num2}")

def subtraction(num1, num2):
    print(f"Subtraction: {num1 - num2}")

def multiplication(num1, num2):
    print(f"Multiplication: {num1 * num2}")

def division(num1, num2):
    try:
        print(f"Division: {num1 / num2}")
    except ZeroDivisionError:
        print("Cannot divide a number by 0.")

def exponention(num):
    print(f"Exponention: {num ** 2}")

def remainder(num1, num2):
    try:
        print(f"Remainder: {num1 % num2}")
    except ZeroDivisionError:
        print("Cannot divide a number by zero.")


def main():
    print("=== Welcome to CLI Calculator ===")
    print("The choices are ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponention")
    print("6. Remainder")
    print("7. Quit()")

    while True:

        choice = input("Enter Your Choice ")

        if choice == "1":
            num1 = int(input("Enter your first number: "))
            num2 = int(input("Enter your second number: "))
            addition(num1,num2)

        elif choice == "2":
            num1 = int(input("Enter your first number: "))
            num2 = int(input("Enter your second number: "))
            subtraction(num1,num2)

        elif choice == "3":
            num1 = int(input("Enter your first number: "))
            num2 = int(input("Enter your second number: "))
            multiplication(num1,num2)

        elif choice == "4":
            num1 = int(input("Enter your first number: "))
            num2 = int(input("Enter your second number: "))
            division(num1,num2)

        elif choice == "5":
            num1 = int(input("Enter your number: "))
            exponention(num1)

        elif choice == "6":
            num1 = int(input("Enter your first number: "))
            num2 = int(input("Enter your second number: "))
            remainder(num1,num2)

        elif choice == "7":
            print("Thank You for Using our CLI Calculator.")
            exit()

        else:
            print("Invalid choice, Please enter valid one.")


main()          