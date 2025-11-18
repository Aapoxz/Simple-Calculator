import math 
choice = input("Select a choice (plus, minus, multiply, division, squareroot): ")

if choice == "squareroot":
    numbersquare = int(input("Number: "))
    print(math.sqrt(numbersquare))

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

elif choice == "plus":
    print(number1 + number2)
elif choice == "minus":
    print(number1 - number2)
elif choice == "multiply":
    print(number1 * number2)
elif choice == "division":
    print(number1 / number2)
