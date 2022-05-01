# Сриниваса Рамануджан – индийский математик, славившийся своей интуицией в области чисел. Когда английский математик Годфри Харди
# навестил его однажды в больнице, он обмолвился, что номером такси, на котором он приехал, было 1729, такое скучное и заурядное число.
# На что Рамануджан ответил: "Нет, нет! Это очень интересное число. Это наименьшее число, выражаемое как сумма двух кубов двумя
# разными способами". Другими словами:
# 1729 = 1^3 + 12^3 = 9^3 + 10^3.
# Напишите программу, которая находит аналогичные интересные числа. В ответе запишите первые 5 чисел в порядке возрастания,
# включая число 1729.
# Примечание. Используйте вложенный цикл.
for n in range(1, 33):
    for k in range(1, 33):
        for m in range(1, 33):
          for t in range(1, 33):
              if n**3 + k**3 == m**3 + t**3 and n!=t and k!=m and k!=t  and  n>k and m>t and n>m:
                n,k ==m, t
                print('n =', n, 'k =', k, 'm =', m, 't=',  t, '=',n **3 + k **3 )
   



# Дано натуральное число. Напишите программу, которая вычисляет:
# количество цифр 3 в нем;
# сколько раз в нем встречается последняя цифра;
# количество четных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
# сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
# Формат входных данных: На вход программе подается одно натуральное число.
# Формат выходных данных: Программа должна вывести значения указанных величин в указанном порядке.
n = int(input())
counter_3 = 0
last_digit = n % 10
counter_LastDigit = 0
counter_2 = 0
summ_5 = 0
prod_7 = 1
counter_05 = 0
while n > 0:
    x = n % 10
    if x == 3:
        counter_3 += 1
    if last_digit == x:
        counter_LastDigit += 1
    if x % 2 == 0:
        counter_2 += 1
    if x > 5:
        summ_5 += x
    if x > 7:
        prod_7 *= x
    if x == 0 or x == 5:
        counter_05 += 1
    n //= 10
print(counter_3)
print(counter_LastDigit)
print(counter_2)
print(summ_5)
print(prod_7)
print(counter_05)

# Дано натуральное число n (n>99). Напишите программу, которая определяет его третью (с начала) цифру.
# Формат входных данных: На вход программе подается одно натуральное число, состоящее как минимум из трех цифр.
# Формат выходных данных: Программа должна вывести его третью (с начала) цифру.
n = int(input())
while n > 999:
    n //= 10
print(n % 10)

# На вход программе подается натуральное число n. Напишите программу, которая печатает звездную рамку размерами n×19.
# Формат входных данных: На вход программе подаётся натуральное число n ∈ [3;19] — высота звездной рамки.
# Формат выходных данных: Программа должна вывести звездную рамку размерами n×19.
# Подсказка. Для печати звездной линии используйте умножение строки на число.
n = int(input())
for i in range(1, n + 1):
    if i == 1 or i == n:
        print('*' * 19)
    else:
        print('*' + ' ' * 17 + '*')


# На обработку поступает последовательность из 4 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10^8.
# Нужно написать программу, которая выводит на экран количество нечётных чисел в исходной последовательности и максимальное нечётное число.
# Если нечётных чисел нет, требуется на экран вывести «NO». Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только одну
# строку и может быть исправлена без изменения других строк.
# Примечание. Обратите внимание, что требуется найти ошибки в имеющейся программе, а не написать свою, возможно,
# использующую другой алгоритм решения.
# Измененный код:
n = 4
count = 0
maximum = -10**8
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

# Исходный код:
n = 4
count = 0
maximum = 999
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = i
            break
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')


# На обработку поступает последовательность из 8 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10^12.
# Нужно написать программу, которая выводит на экран количество делящихся нацело на 4 чисел в исходной последовательности и максимальное
# делящееся нацело на 4 число. Если делящихся нацело на 4 чисел нет, требуется на экран вывести «NO». Программист торопился и
# написал программу неправильно.
# Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только одну
# строку и может быть исправлена без изменения других строк.
# Примечание. Обратите внимание, что требуется найти ошибки в имеющейся программе, а не написать свою, возможно,
# использующую другой алгоритм решения.
# Измененный код:
n = 8
count = 0
maximum = -10**12
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')


# Исходный код:
n = 7
count = 0
maximum = 1000
for i in range(1, n + 1):
    x = int(input())
    if x // 4 == 0:
        count += 1
        if x < maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')



# На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран сумму чётных цифр этого числа или 0,
# если чётных цифр в записи нет. Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только одну строку
# и может быть исправлена без изменения других строк.
# Примечание. Обратите внимание, что требуется найти ошибки в имеющейся программе, а не написать свою,
# возможно, использующую другой алгоритм решения.
# Измененный код:
n = int(input())
s = 0
while n > 0:
    if n % 2 == 0:
        s += n % 10
    n //= 10
print(s)

# Исходный код:
n = input()
s = 0
while n > 10:
    if n % 2 == 1:
        s = n % 10
    n //= 10
print(s)