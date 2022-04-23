# определение макс и мин цифры в введенном числе
n = int(input())
maximum = max(str(n))
minimum = min(str(n))
print('Максимальная цифра равна', maximum)
print('Минимальная цифра равна', minimum)


# вывод цифр введенного числа в обратном порядке
n = int(input())
while n > 0:
    last_digit = n % 10
    print(last_digit)
    n = n // 10


# определение сколько в введенном числе сидит других предопределенных чисел, чтобы получить введенное число
n = int(input())
counter = 0
while n >= 25:
    counter += 1
    n -= 25
while n >= 10:
    counter += 1
    n -= 10
while n >= 5:
    counter += 1
    n -= 5
while n >= 1:
    counter += 1
    n -= 1
print(counter)

# цикл со счетчиком цифры 5 с остановкой при вводе отрицательного числа
x = int(input())
counter = 0
while x >= 0 and x < 6:
    if x == 5:
        counter += 1
    x = int(input())
print(counter)



# цикл с вычислением суммы введенных чисел с остановкой при вводе отрицательного числа
x = int(input())
y = 0
while x >= 0:
    y = y + x
    x = int(input())
print(y)



# цикл с остановкой по делению числа с остатком
x = int(input())
while x % 7 == 0:
    print(x)
    x = int(input())


# цикл с остановкой по введенному слову и счетчиком введенных слов
i = input()
counter = 0
while i != 'стоп' and i != 'хватит' and i != 'достаточно':
    counter += 1
    i = input()
print(counter)



# цикл с остановкой по введенному слову
i = input()
while i != 'КОНЕЦ' and i != 'конец':
    print(i)
    i = input()
    



# c for  и счетчиками закончили, выше начинается while




# последовательность Фибоначчи
n= int(input())
member1 = 0
member2 = 1
for i in range(n):
    member1, member2 = member2, member1 + member2
    print(member1, end=' ')



# определение четности введенных чисел
flag = True
for i in range (10):
    n = int(input())
    if n % 2 != 0:
        flag = False
if flag == True:
    print('YES')
else:
    print('NO')



# вывод наибольшего и второго наибольшего чисел из диапазона вводимых чисел, кол-во чисел = первому введенному числу
n = int(input())
large = 0
prelarge = 1
for i in range(n):
    m = int(input())
    if m > large:
        prelarge = large
        large = m
    elif m > prelarge:
        prelarge = m
print(large)
print(prelarge)




# вычисление выражения с чередующимися + и -
n = int(input())
total = 0
for i in range(n + 1):
    if i % 2 == 0:
        total -= i
    elif i % 2 != 0:
        total += i
print(total)


# сумма делителей введенного числа (когда число делится без остатка), которое является верхней границей диапазона
total = 0
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        total += i
print(total)



# произведение введенных чисел не равных 0
total = 1
for i in range(10):
    x = int(input())
    if x != 0:
        total *= x
print(total)


# вычисление факториала по введенному числу
n = int(input())
total = 1
for i in range(1, n + 1):
    total *= i
print(total)



# подсчет суммы чисел из введенного диапазона по заданному условию
n = int(input())
total = 0
for i in range(1, n + 1):
    if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
        total += i
print(total)


# асимптотическое приближение
from math import *
n = int(input())
total = 0
for i in range(1, n + 1):
    total = total + 1 / i
print(total - log(n))


# подсчет суммы введенных чисел, число введенных чисел равно введенному первым числу
n = int(input())
total = 0
for i in range(n):
    m = int(input())
    total += m
print(total)



# подсчет кол-ва чисел в введенном диапазоне по условию
a, b = int(input()), int(input())
counter = 0
for i in range(a, b + 1):
    if i**3 % 10 == 4 or i % 10 == 9:
        counter += 1
print(counter)



# таблица умножения на введенное число
n = int(input())
for i in range(1, 11):
    print(n, 'x', i, '=', n * i)


# вывод чисел из введенного диапазона по заданным условиям
m, n = int(input()), int(input())
for i in range(m, n + 1):
    if i % 17 == 0 or (i % 5 == 0 and i % 3 == 0) or i % 10 == 9:
        print(i)



# последовательный вывод нечетных чисел из заданного диапазона в порядке убывания
m, n = int(input()), int(input())
for i in range(m, n - 1, -1):
    if i % 2 != 0:
        print(i)
 


# последовательный вывод чисел из заданного диапазона в порядке возрастания или убывания
m, n = int(input()), int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)
elif m > n:
    for i in range(m, n - 1, -1):
        print(i)
else:
    print(m)


# последовательный вывод чисел из заданного диапазона
m, n = int(input()), int(input())
for i in range(m, n + 1):
    print(i)



# рост популяции по введенным значениям: кол-во на старте, % роста, кол-во дней размножения
m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    print(i + 1, float(m))
    m = m + m * p / 100



# вывод прямоугольного равнобедренного треугольника из **** по заданному чисоу = длине стороны
n = int(input())
for i in range(n + 1):
    print('*' * (n - i))



# квадраты чисел от 0 до введенного значения
n = int(input())
for i in range(n + 1):
    print('Квадрат числа', i, 'равен', i**2)




# вывод вводимой строки с нумерацией повторения
st = str(input())
for i in range(10):
    print(i, st)



# строки из ***** по заданному количеству
n = int(input())
for i in range(n):
    print('*' * 19)



# просто вывод заранее заданных строк
for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')



# вывод введенной строки введенное количество раз
st = str(input())
num = int(input())
for i in range(num):
    print(st)




# вывод строки 10 раз
for i in range(10):
    print('Python is awesome!')


