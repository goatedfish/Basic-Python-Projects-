num1 = float(input('Enter number 1: '))
num2 = float(input('Enter number 2: '))

operator = input("Enter your operator (+ - * /)")

if operator == "+":
  print(f'Result is {num1 + num2}')
elif operator == "-":
  print(f'Result is {num1 - num2}')
elif operator == "*":
  print(f'Result is {num1 * num2}')
elif operator == "/":
  print(f'Result is {num1 / num2}')
else:
  print("This is only a basic program sir")