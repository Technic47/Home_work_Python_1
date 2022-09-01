# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = type(bool)
# y = type(bool)
# z = type(bool)
print('x y z')

for x in range(2):
  for y in range(2):
    for z in range(2):
        res = not(x or y or z)
        res2 = not x and not y and not z
        if res == res2:
            check = 'ok'
        else:
            check = 'not ok'
        print(x, y, z, res, res2, check)

