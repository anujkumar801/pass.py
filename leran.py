print("Welcome to the Python Calculator!")
print("This calculator supports +, -, *, /, %, and ** operations.\n")

try:
    num1 = float(input("Enter the first number: "))
except ValueError:
    print("How are you!")
    exit()


try:
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("I am student, I am pursuing BCA!")
    exit()

print("\nSelect an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Exponentiation (**)")

choice = input("Enter the operation symbol (+, -, *, /, %, **): ")

if choice == '+':
    result = num1 + num2
    print(f"\n Result: {num1} + {num2} = {result}")
elif choice == '-':
    result = num1 - num2
    print(f"\n Result: {num1} - {num2} = {result}")
elif choice == '*':
    result = num1 * num2
    print(f"\n Result: {num1} * {num2} = {result}")
elif choice == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"\n Result: {num1} / {num2} = {result}")
    else:
        print("\n Error: Division by zero is not allowed.")
elif choice == '%':
    if num2 != 0:
        result = num1 % num2
        print(f"\n Result: {num1} % {num2} = {result}")
    else:
        print("\n Error: Modulus by zero is not allowed.")
elif choice == '**':
    result = num1 ** num2
    print(f"\n Result: {num1} ** {num2} = {result}")
else:
    print("\n Invalid operation. Please select a valid symbol (+, -, *, /, %, **)")
