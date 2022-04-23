# ход ферзя
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):
    print('YES')
elif x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')


# ход коня
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x1 - x2 == 1 and (y1 - y2 == 2 or y2 - y1 == 2):
    print('YES')
elif x2 - x1 == 1 and (y1 - y2 == 2 or y2 - y1 == 2):
    print('YES')
elif x2 - x1 == 2 and (y1 - y2 == 1 or y2 - y1 == 1):
    print('YES')
elif x1 - x2 == 2 and (y2 - y1 == 1 or y1 - y2 == 1):
    print ('YES')
else:
    print('NO')


# ход слона
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):
    print('YES')
else:
    print('NO')



n = int(input())
if n % 2 != 0:
    print('YES')
elif 6 <= n <=20 and n % 2 == 0:
    print('YES')
else:
    print('NO')


n = int(input())
if n == 1:
    print('I')
elif n == 2:
    print('II')
elif n == 3:
    print('III')
elif n == 4:
    print('IV')
elif n == 5:
    print('V')
elif n == 6:
    print('VI')
elif n == 7:
    print('VII')
elif n == 8:
    print('VIII')
elif n == 9:
    print('IX')
elif n == 10:
    print('X')
else:
    print('ошибка')


age = int(input())
sex = input()
if 10 <= age <= 15 and sex == 'f':
    print('YES')
else:
    print('NO')


c1, l1, c2, l2 = int(input()), int(input()), int(input()), int(input())
if (c1 + l1) % 2 == 0 and (c2 + l2) % 2 == 0:
    print('YES')
elif (c1 + l1) % 2 != 0 and (c2 + l2) % 2 != 0:
    print('YES')
else:
    print('NO')



y = int(input())
if y % 100 == 0:
    print('YES')
else:
    print("NO")
