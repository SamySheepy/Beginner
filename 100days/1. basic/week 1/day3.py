num1 = input("Enter a number: ")
num1 = int(num1)
print(f"Number doubled: {num1 * 2}")

num2 = int(input("Enter another number: "))
result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}")

a = 10
b = 5
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
#chia làm tròn đến số nguyên
print(f"Floor Division: {a // b}")
#Chia lấy số dư
print(f"Modulus: {a % b}")
#a mũ b
print(f"Exponentiation: {a ** b}")

# Simple Calculator
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2 if number2 != 0 else "Cannot divide by zero."
print("\n--- Calculaor Results ---")
print(f"Addition: {number1} + {number2} = {addition}")
print(f"Subtraction: {number1} - {number2} = {subtraction}")
print(f"Multiplication: {number1} x {number2} = {multiplication}")
print(f"Division: {number1} / {number2} = {division}")

#----challenge----
number3 = float(input("Enter the third number: "))
number4 = float(input("Enter the fourth number: "))
addition = number3 + number4
subtraction = number3 - number4
multiplication = number3 * number4
division = number3 / number4 if number4 != 0 else "Cannot divide by zero."
floordivision = number3 // number4 if number4 != 0 else "Cannot divide by zero."
modulus = number3 % number4
exponentiation = number3 ** number4
operation = input("Choose to plus/minus/multiply/divide/floordivision/modulus/exponentiation/all: ")
if operation == "plus" :
    print(f"Addition: {number3} + {number4} = {addition}")
elif operation == "minus" :
    print(f"Subtraction: {number3} - {number4} = {subtraction}")
elif operation == "multiply" :
    print(f"Multiplication: {number3} x {number4} = {multiplication}")
elif operation == "divide" :
    print(f"Division: {number3} / {number4} = {division}")
elif operation == "floordivision" :
    print(f"Floor Division: {number3} // {number4} = {floordivision}")
elif operation == "modulus" :
    print(f"Modulus: {number3} % {number4} = {modulus}")
elif operation == "exponentiation" :
    print(f"Exponentiation: {number3} ** {number4} = {exponentiation}")
else:
    print(f"Addition: {number3} + {number4} = {addition}")
    print(f"Subtraction: {number3} - {number4} = {subtraction}")
    print(f"Multiplication: {number3} x {number4} = {multiplication}")
    print(f"Division: {number3} / {number4} = {division}")
    print(f"Floor Division: {number3} // {number4} = {floordivision}")
    print(f"Modulus: {number3} % {number4} = {modulus}")
    print(f"Exponentiation: {number3} ** {number4} = {exponentiation}")
