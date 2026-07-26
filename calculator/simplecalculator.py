print("Welcome to Shaheryar Calculator")
num1= float(input("Enter First Number " ))
num2= float(input("second number "))

operator = input("Enter operator +, -, *, /: ")

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error! Cannot divide by zero.")

else:
    print("Invalid operator.")