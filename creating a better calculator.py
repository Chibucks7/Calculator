#creating a better calculator

num1 = float(input("Enter a first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter a second number: "))

if op == "+":
    print(num1 + num2)
if op == "-":
    print(num1 - num2)
if op == "/":
    print (num1 / num2)
if op == "*":
    print(num1 * num2)
else:
    print("invalid operator")
