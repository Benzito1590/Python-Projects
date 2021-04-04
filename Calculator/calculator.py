def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
print('This is a calculator')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
x = 1
while x == 1:
     choice = input('Choose from the options(1, 2, 3, 4): ')
     num1 = int(input('Enter First Number: '))
     num2 = int(input('Enter Second Number: '))
     if choice == '1':
      print(f'{num1} + {num2} = {add(num1, num2)}')
     if choice == '2':
      print(f'{num1} - {num2} = {sub(num1, num2)}')
     if choice == '3':
      print(f'{num1} * {num2} = {mul(num1, num2)}')
     if choice == '4':
      print(f'{num1} / {num2} = {div(num1, num2)}')