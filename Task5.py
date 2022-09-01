# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

A = []
B = []

A.append(int(input('Coordinate A(x,..,..) ')))
A.append(int(input('Coordinate A(..,y,..) ')))
A.append(int(input('Coordinate A(..,..,z) ')))
B.append(int(input('Coordinate B(x,..,..) ')))
B.append(int(input('Coordinate B(..,y,..) ')))
B.append(int(input('Coordinate B(..,..,z) ')))


def SqrSum(a):
    res = (B[a] - A[a]) ** 2
    return res


dist = type(float)
dist = (SqrSum(0) + SqrSum(1) + SqrSum(2)) ** 0.5
print(round(dist, 3))
