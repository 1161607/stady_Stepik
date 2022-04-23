# площадь правильного многоугольника
from math import *
n = int(input())
a = float(input())
print((n * pow(a, 2)) / (4 * tan(pi / n)))



# вещественные корни квадратного уравнения
from math import *
a, b, c = float(input()), float(input()), float(input())
D = pow(b, 2) - 4 * a * c
if D > 0:
    x1 = (- b + sqrt(D)) / (2 * a)
    x2 = (- b - sqrt(D)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
elif D == 0:
    print(- b / (2 * a))
elif D < 0:
    print('Нет корней')



# потолок и пол числа
from math import *
x = float(input())
print(ceil(x) + floor(x))


# синус, косинус и тангенс + перевод радианов в градусы
from math import *
x = radians(float(input()))
print(sin(x) + cos(x) + pow(tan(x), 2))



# среднее арифметическое, геометрическое, гармоническое и квадратичное
from math import *
a, b = float(input()), float(input())
print((a + b) / 2) # арифметическое
print(sqrt(a * b)) # геометрическое
print(2 * a * b / (a + b)) # гармоническое
print(sqrt((a**2 + b**2) / 2)) # квадратичное



# площадь круга и длина окружности
from math import *
R = float(input())
print(pi * pow(R, 2))
print(2 * pi * R)



# Евклидово расстояние
from math import *
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)))
