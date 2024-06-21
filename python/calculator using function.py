import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Cannot calculate square root of a negative number."
    else:
        return math.sqrt(x)

print("Welcome to Simple Scientific Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponentiate")
print("6. Square Root")

choice = input("Enter choice (1/2/3/4/5/6): ")

if choice in ('1', '2', '3', '4', '5'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", exponentiate(num1, num2))
elif choice == '6':
    num = float(input("Enter a number: "))
    print("Result:", square_root(num))
else:
    print("Invalid Input")

