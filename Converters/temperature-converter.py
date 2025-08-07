temp = float(input('Enter the temperature: '))
unit = input('Enter the unit of your temperature: Celcius/Farenheit/Kelvin(c f k)')
unit_final = input('Enter the unit in which you want to check the temperature:')

if unit == 'c':
  if unit_final == unit:
    print('Please use a different unit')
  elif unit_final == 'f':
    result = 1.8*temp + 32
    unt = 'Farenheits'
  elif unit_final == 'k':
    result = temp + 273.15
    unt = "Kelvin"
  else:
    print(f'{unit_final} is not valid')
elif unit == 'f':
  if unit_final == unit:
    print('Please use a different unit')
  elif unit_final == 'c':
    result = (5/9)*temp - 160/9
    unt = 'Celcius'
  elif unit_final == 'k':
    result = (5/9)*temp - 160/9 - 273.15
    unt = 'Kelvin'
  else:
    print(f'{unit_final} is not valid')
elif unit == 'k':
  if unit_final == unit:
    print('Please use a different unit')
  elif unit_final == 'c':
    result = temp - 273.15
    unt = 'Celcius'
  elif unit_final == 'f':
    result = 1.8*(temp - 273.15) + 32
    unt = 'Farenheits'
  else:
    print(f'{unit_final} is not valid')
else:
  print(f'{unit} is not valid')
print(f'Temperature = {result}{unt}')