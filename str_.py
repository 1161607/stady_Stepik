# проверка корректности email
a = str(input())
if '@' in a and '.' in a:
    print('YES')
else:
    print('NO')


# проверка наличия любого из двух слов в строке
a = str(input())
if 'суббота' in a or 'воскресенье' in a:
    print('YES')
else:
    print('NO')



# проверка наличия слова в строке
a = str(input())
if 'синий' in a:
    print('YES')
else:
    print('NO')


# проверка длин строк на соответствие арифметической прогрессии
a = len(input())
b = len(input())
c = len(input())
if a == (b + c) / 2 or b == (a + c) / 2 or c == (a + b) / 2:
    print('YES')
else:
    print('NO')



# длина строки и вывод строки по порядку в зависимости от длины
c1 = input()
c2 = input()
c3 = input()
top = min(len(c1), len(c2), len(c3))
down = max(len(c1), len(c2), len(c3))
if top == len(c1):
    print(c1)
elif top == len(c2):
    print(c2)
elif top == len(c3):
    print(c3)
if down == len(c1):
    print(c1)
elif down == len(c2):
    print(c2)
elif down == len(c3):
    print(c3)
