# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек
# в этой четверти (x и y).

number = int(input('Input number: '))

if number == 1:
    print('x = 1...inf \ny = 1...inf')
elif number == 2:
    print('x = 1...inf \ny = -1...-inf')
elif number == 3:
    print('x = -1...-inf \ny = -1...-inf')
elif number == 4:
    print('x = -1...-inf \ny = 1...inf')
else:
    print('Wrong number.')