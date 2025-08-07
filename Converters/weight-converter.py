# simply converts weight entered by user from kilograms to pounds

weight = float(input('Enter your weight(in kg): '))
result = round(weight * 2.20462,3)

print(f'YOUR WEIGHT IN POUNDS IS: {result}')