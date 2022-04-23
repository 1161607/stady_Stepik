# манхэттенское расстояние
p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
print(abs(p1 - q1) + abs(p2 - q2))



# сумма модулей чисел
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
print(abs(a) +abs(b) + abs(c) + abs(d) + abs(e))


# сравнение цифр и их разности в 3-хзначном числе
n = int(input())
first = n // 100
second = n // 10 % 10
third = n % 10
if max(first, second, third) - min(first, second, third) == (first + second + third - max(first, second, third) - min(first, second, third)):
    print ('Число интересное')
else:
    print('Число неинтересное')



# сортировка 3-х чисел
a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))
print(a + b + c - max(a, b, c) - min(a, b, c))
print(min(a, b, c))


# наибольшее и наименьшее
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print('Наименьшее число =', min(a, b, c, d, e))
print('Наибольшее число =', max(a, b, c, d, e))



# вывод цифр после запятой
x = float(input())
print(x - int(x))



#первая цифра после запятой
x = float(input())
y = int(x * 10)
print(y % 10)



# возраст собаки в человеческих годах
n = int(input())
if n <= 2:
    print(n * 10.5)
else:
    print(2 * 10.5 + n * 4 - 8)


# фаренгейты в цельсии
f = float(input())
print( 5 / 9 * (f - 32))


# обратное число
x = float(input())
if x != 0:
    print(1 / x)
else:
    print('Обратного числа не существует')


# встреча старушек
s = float(input())
v1 = float(input())
v2 = float(input())
print(s / (v1 + v2))


# площадь треугольника
a = float(input())
b = float(input())
print(0.5 * a * b)
