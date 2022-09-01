# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет,
# является ли этот день выходным.

number = int(input('Input number: '))

if number in range(6, 8):
    print('This is Weekend')
elif number in range(1, 6):
    print('This is a working day')
else:
    print('This is wrong number')
