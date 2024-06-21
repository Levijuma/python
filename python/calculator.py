def calculator():
 print("This is my calculator")

print("select an option to perform:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

operation=input()

if operation == "1":
 num1=int(input("Enter first number"))
 num2=int(input("Enter second number"))
 print(f"the sum of {num1} and {num2} is {num1+num2}")

if operation == "2":
 num1=int(input("Enter first number"))
 num2=int(input("Enter second number"))
 print(f"the difference of {num1} and {num2} is {num1-num2}")


if operation == "3":
 num1=int(input("Enter first number"))
 num2=int(input("Enter second number"))
 print(f"the product of {num1} and {num2} is {num1*num2}")

if operation == "4":
 num1=int(input("Enter first number"))
 num2=int(input("Enter second number"))
 print(f"the quotient of {num1} and {num2} is {num1/num2}")

 calculator()







