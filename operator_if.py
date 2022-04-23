# ход короля
column1 = int(input())
line1 = int(input())
column2 = int(input())
line2 = int(input())
if 1<= column1 <=8 and 1<= line1 <=8 and 1<= column2 <=8 and 1<= line2 <=8:
    if (column1 - 1) <= column2 <= (column1 + 1) and (line1 - 1) <= line2 <= (line1 + 1):
        print('YES')
    else:
        print('NO')
else:
    print('Неверные входные данные')

# ход ладьи
column1 = int(input())
line1 = int(input())
column2 = int(input())
line2 = int(input())
if 1<= column1 <=8 and 1<= line1 <=8 and 1<= column2 <=8 and 1<= line2 <=8:
    if column1 == column2 or line1 == line2:
        print('YES')
    else:
        print('NO')
else:
    print('Неверные входные данные')



n = int(input())
if n > 0 and n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('YES')
else:
    print('NO')


ab = int(input())
bc = int(input())
ca = int(input())
if ab < bc + ca and bc < ab + ca and ca < ab + bc:
    print('YES')
else:
    print('NO')


x = int(input())
if 999 < x < 10000 and (x % 7 == 0 or x % 17 == 0):
    print('YES')
else:
    print('NO')


    
x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')
