n = int(input())
a = n // 10000
b = n % 10000 // 1000
c = n % 1000 // 100
d = n % 100 // 10
e = n % 10
print('Цифра в позиции десятков тысяч равна', a)
print('Цифра в позиции тысяч равна', b)
print('Цифра в позиции сотен равна', c)
print('Цифра в позиции десятков равна', d)
print('Цифра в позиции единиц равна', e)

num = int(input())
zero_digit = num // 1000
first_digit = num // 100 % 10
second_digit = num // 10 % 10
third_digit = num % 10
print('Цифра в позиции тысяч равна', zero_digit)
print('Цифра в позиции сотен равна', first_digit)
print('Цифра в позиции десятков равна', second_digit)
print('Цифра в позиции единиц равна', third_digit)

x = int(input())
a = x // 100
b = x // 10 % 10
c = x % 10
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')

x = int(input())
digit1 = x // 100
digit2 = (x // 10) % 10
digit3 = x % 10
y = digit1 + digit2 + digit3
z = digit1 * digit2 * digit3
print('Сумма цифр =', y)
print('Произведение цифр =', z)



