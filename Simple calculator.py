#Simple calculator
import math
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exponentiation\n6.Square Root\n7.Logarithm")
choice = input("Enter your choice (1-7): ")
if choice in ['1', '2', '3', '4']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        print(f"The sum of {num1} and {num2} is {num1 + num2}")
    elif choice == '2':
        print(f"The difference between {num1} and {num2} is {num1 - num2}")
    elif choice == '3':
        print(f"The product of {num1} and {num2} is {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"The quotient of {num1} and {num2} is {num1 / num2}")
        else:
            print("Error: Division by zero")
elif choice == '5':
    base = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))
    print(f"{base} raised to the power of {exponent} is {math.pow(base, exponent)}")
elif choice == '6':
    num = float(input("Enter a number: "))
    if num >= 0:
        print(f"The square root of {num} is {math.sqrt(num)}")
    else:
        print("Error: Cannot compute square root of a negative number")
elif choice == '7':
    num = float(input("Enter a number: "))
    if num > 0:
        print(f"The natural logarithm of {num} is {math.log(num)}")
    else:
        print("Error: Cannot compute logarithm of non-positive numbers")
else:
    print("Invalid choice. Please select a number between 1 and 7.")