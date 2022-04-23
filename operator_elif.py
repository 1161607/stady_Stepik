# пересечение двух отрезков
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if b1 == a2:
    print(b1)
elif a1 == a2 and b1 == b2:
    print(a1, b1)
elif a2 < a1 < b2 < b1:
    print(a1, b2)
elif a1 < a2 < b1 < b2:
    print(a2, b1)
elif a2 < a1 < b1 < b2:
    print(a1, b1)
elif a1 < a2 < b2 < b1:
    print(a2, b2)
elif a1 == a2 and b1 < b2:
    print(a1, b1)
elif a2 < a1 and b1 == b2:
    print(a1, b1)
elif b2 == a1:
    print(a1)
elif b1 == b2:
    print(a2, b2)
else:
    print('пустое множество')


# определение выпавшего цвета на рулетке от выпавшего номера
n = int(input())
if 0 <= n <= 36:
    if n == 0:
        print('зеленый')
    elif (0 < n <= 10 or 18 < n <= 28) and n % 2 == 0:
        print('черный')
    elif (10 < n <= 18 or 28 < n <= 36) and n % 2 !=0:
        print('черный')
    else:
        print('красный')
else:
    print('ошибка ввода')


# смешивание цветов
a = input()
b = input()
if a == 'красный' and b == 'красный':
    print('красный')
elif a == 'синий' and b == 'синий':
    print('синий')
elif a == 'желтый' and b == 'желтый':
    print('желтый')
elif (a == 'красный' and b == 'синий') or (b == 'красный' and a == 'синий'):
    print('фиолетовый')
elif (a == 'красный' and b == 'желтый') or (b == 'красный' and a == 'желтый'):
    print('оранжевый')
elif (a == 'синий' and b == 'желтый') or (b == 'синий' and a == 'желтый'):
    print('зеленый')
else:
    print('ошибка цвета')

# калькулятор
x = int(input())
y = int(input())
a = input()
if a == '+':
    print(x + y)
elif a == '-':
    print(x - y)
elif a == '*':
    print(x * y)
elif a == '/' and y != 0:
    print(x / y)
elif y == 0:
    print('На ноль делить нельзя!')
else:
    print('Неверная операция')

# вывод значения от введенного числа
w = int(input())
if w < 60:
    print ('Легкий вес')
elif w < 64:
    print('Первый полусредний вес')
elif w < 69:
    print ('Полусредний вес')

# выбор среднего числа из ряда
n = int(input())
if n == 2:
    print(28)
elif (n <= 7 and n % 2 != 0) or (7 < n and n % 2 == 0):
    print(31)
else:
    print(30)

# вид треугольника
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a == b or b == c or a == c:
    print('Равнобедренный')
else:
    print("Разносторонний")


# кто быстрее
n, k = int(input()), int(input())
if n > k:
    print('NO')
elif k > n:
    print('YES')
else:
    print("Don't know")
