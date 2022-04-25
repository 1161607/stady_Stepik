# На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран его первую (старшую) цифру.
# Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 2). Известно, что каждая ошибка затрагивает только одну строку и может
# быть исправлена без изменения других строк.
# Измененный код:
n = int(input())
while n > 0:
    digit = n % 10
    n = n // 10
print(digit)

# Исходный код:
n = int(input())
while n > 0:
    n %= 10
print(n)




# На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран максимальную цифру числа, кратную 3.
# Если в числе нет цифр, кратных 3, требуется на экран вывести «NO». Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 5). Известно, что каждая ошибка затрагивает только одну строку и может быть
# исправлена без изменения других строк.
# Примечание 1. Число 0 делится на любое натуральное число.
# Примечание 2. При необходимости вы можете добавить нужные строки кода.
# Измененный код:
n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit % 3 != 0:
    print('NO')
else:
    print(max_digit)

# Исходный код:
n = int(input())
max_digit = n % 10
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit < max_digit:
            digit = max_digit
    n = n % 10
if max_digit == 0:
    print('NO')
else:
    print(max_digit)



# На обработку поступает последовательность из 7 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10^6.
# Нужно написать программу, которая подсчитывает и выводит сумму всех чётных чисел последовательности или 0, если чётных чисел
# в последовательности нет. Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 4). Известно, что каждая ошибка затрагивает только одну строку и может быть
# исправлена без изменения других строк.
# Примечание 1. Число x не превышает по абсолютной величине 10^6, если -10^6 <= x <= 10^6.
# Примечание 2. При необходимости вы можете добавить необходимые строки кода.
# Измененный код:
s = 0
for i in range(1, 8):
    n = int(input())
    if n % 2 == 0:
        s = s + n
if s != 0:
    print(s)
else:
    print(0)

# Исходный код:
s = 1
for i in range(1, 7):
    n = input()
    if i % 2 == 0:
        s = s + n
print(s)




# На обработку поступает последовательность из 10 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10^6.
# Нужно написать программу, которая выводит на экран сумму всех отрицательных чисел последовательности и максимальное отрицательное
# число в последовательности. Если отрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал
# программу неправильно.
# Найдите все ошибки в этой программе (их ровно 5). Известно, что каждая ошибка затрагивает только одну строку и может
# быть исправлена без изменения других строк.
# Примечание 1. Число x не превышает по абсолютной величине 10^6, если -10^6 <= x <= 10^6
# Примечание 2. При необходимости вы можете добавить необходимые строки кода.
# Измененный код:
mx = -10**6
s = 0
for i in range(1, 11):
    x = int(input())
    if x < 0:
        s += x
    if 0 > x > mx:
        mx = x
if s < 0:
    print(s)
    print(mx)
else:
    print('NO')

# Исходный код:
mx = 0
s = 0
for i in range(11):
    x = int(input())
    if x < 0:
        s = x
    if x > mx:
        mx = x
print(s)
print(mx)



# На обработку поступает последовательность из 10 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10^6.
# Нужно написать программу, которая выводит на экран количество неотрицательных чисел последовательности и их произведение.
# Если неотрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 4). Известно, что каждая ошибка затрагивает только одну строку и может
# быть исправлена без изменения других строк.
# Примечание 1. Число x не превышает по абсолютной величине 10^6, если -10^6 <= x <= 10^6.
# Примечание 2. При необходимости вы можете добавить необходимые строки кода.
# Измененный код:
count = 0
p = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        p = p * x
        count = count + 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')

# Исходный код:
count = 0
p = 0
for i in range(1, 10):
    x = int(input())
    if x > 0:
        p = p * x
        count = count + 1
if count > 0:
    print(x)
    print(p)
else:
    print('NO')



# ЗАДАЧИ НА РЕВЬЮ КОДА


# На вход программе подается натуральное число nn. Напишите программу, которая выводит числа от 1 до n включительно за исключением:
# чисел от 5 до 9 включительно;
# чисел от 17 до 37 включительно;
# чисел от 78 до 87 включительно.
n = int(input())
for i in range(1, n +1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)


# На вход программе подается число n > 1. Напишите программу, которая выводит его наименьший отличный от 1 делитель.
n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        break
print(i)


# Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
n = int(input())
last_number = n % 10
sequence = True
while n > 0:
    last_digit = n % 10
    if last_digit < last_number:
        sequence = False
    else:
        last_number = last_digit
    n = n // 10
if sequence == True:
    print('YES')
else:
    print('NO')



# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
n = int(input()) # вариант решения без цикла
if max(str(n)) == min(str(n)): 
    print('YES')
else:
    print('NO')

n = int(input()) # вариант решения с циклом и флагом
last_number = n % 10
equality = True
while n > 0:
    if last_number != n % 10:
        equality = False
    n = n // 10
if equality == True:
    print('YES')
else:
    print('NO')

# Дано натуральное число n (n>9). Напишите программу, которая определяет его вторую (с начала) цифру.
n = int(input())
while n > 10:
    second_number = n % 10
    n = n // 10
print(second_number)

# Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
n = int(input())
summ = 0
counter = 0
product = 1
last_number = n % 10
while n > 0:
    last_digit = n % 10
    summ += last_digit
    counter += 1
    product *= last_digit
    n = n // 10
print(summ, counter, product, summ / counter, last_digit, last_digit + last_number, sep = '\n')



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


