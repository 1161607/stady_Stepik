# Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и использует шифр Цезаря.
# Это их и подвело, ведь данный шифр очень простой. Однако в постапокалипсисе люди плохо знают все тонкости довоенного мира,
# поэтому ученые из НКР не могут понять как именно нужно декодировать данные сообщения. Напишите программу для декодирования этого шифра.
# Формат входных данных: В первой строке дается число n (1 ≤ n ≤ 25) – сдвиг, во второй строке даётся закодированное сообщение
# в виде строки со строчными латинскими буквами.
# Формат выходных данных: Программа должна вывести одну строку – декодированное сообщение. Обратите внимание, что нужно
# декодировать сообщение, а не закодировать.
n = int(input())
s = input()
for i in s:
    x = ord(i) - n
    if x < 97:
        x += 26
    print(chr(x), end='')


# На вход программе подается строка текста. Напишите программу, которая переводит каждый ее символ в соответствующий
# ему код из таблицы символов Unicode.
# Формат входных данных: На вход программе подается строка текста.
# Формат выходных данных: Программа должна вывести кодовые значения символов строки разделенных одним символом пробела.
s = input()
for i in range(len(s)):
    print(ord(s[i]), end=' ')


# На вход программе подаются два числа a и b. Напишите программу, которая для каждого кодового значения
# в диапазоне от a до b (включительно), выводит соответствующий ему символ из таблицы символов Unicode.
# Формат входных данных: На вход программе подается два натуральных числа, каждое на отдельное строке.
# Формат выходных данных: Программа должна вывести текст в соотвествии с условием задачи.
a, b = int(input()), int(input())
for i in range(a, b + 1):
    print(chr(i), end=' ')


# На вход программе подается строка текста, в которой буква «h» встречается минимум два раза. Напишите программу,
# которая удаляет из этой строки первое и последнее вхождение буквы «h», а также все символы, находящиеся между ними.
# Формат входных данных: На вход программе подается строка текста.
# Формат выходных данных: Программа должна вывести текст в соответствии с условием задачи.
s = input()
first = s.find('h')
last = s.rfind('h')
print(s[:first] + '' + s[last + 1:])


# На вход программе подается строка текста. Если в этой строке буква «f» встречается только один раз, выведите её индекс.
# Если она встречается два и более раз, выведите индекс её первого и последнего вхождения на одной строке, разделенных
# символом пробела. Если буква «f» в данной строке не встречается, следует вывести «NO».
# Формат входных данных: На вход программе подается строка текста.
# Формат выходных данных: Программа должна вывести текст в соответствии с условием задачи.
s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') > 1:
    print(s.find('f'), s.rfind('f'))
else:
    print('NO')


# На вход программе подается строка текста. Напишите программу, которая выводит на экран символ, который появляется наиболее часто.
# Формат входных данных: На вход программе подается строка текста. Текст может содержать строчные и заглавные
# буквы английского и русского алфавита, а также цифры.
# Формат выходных данных: Программа должна вывести символ, который появляется наиболее часто.
# Примечание 1. Если таких символов несколько, следует вывести последний по порядку символ.
# Примечание 2. Следует различать заглавные и строчные буквы, а также буквы русского и английского алфавита.
s = input()
max1 = 0
max2 = 0
for i in s:
    if s.count(i) >= max1:
        max1 = s.count(i)
        max2 = i
print(max2)


# На вход программе подается строка текста. Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru.
# Формат входных данных: На вход программе подается строка текста.
# Формат выходных данных: Программа должна вывести «YES» если введенная строка заканчивается подстрокой .com или .ru и «NO» в противном случае.
s = input()
if s.endswith('.com', '.ru') == True:
    print('YES')
else:
    print('NO')


# На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.
# Формат входных данных: На вход программе подается строка текста.
# Формат выходных данных: Программа должна вывести количество цифр в данной строке.
s = input()
counter = 0
for i in range(len(s)):
    if s[i] in '0123456789':
        counter += 1
print(counter)



# Джим Хоппер с помощью радиоприемника пытается получить сообщение Оди. На приемник ему поступает nn различных
# последовательностей кода Морзе. Декодировав их, он получает последовательности из цифр и строчного латинского алфавита,
# при этом во всех сообщениях Оди содержится число 11, причем минимум 3 раза. Помогите определить Джиму количество сообщений от Оди.
# Формат входных данных: В первой строке подаётся число n – количество сообщений, в последующих nn строках вводятся строки,
# содержащие латинские строчные буквы и цифры.
# Формат выходных данных: Программа должна вывести количество строк в которых содержится число 11 минимум 3 раза.
# Примечание: Числа 11 необязательно должны быть разделены другими символами, нужно подсчитать вхождение
# последовательности символов "11", т.е. например в строке "111" содержится одна такая последовательность, в то время как в "1111" их уже две.
n = int(input())
counter = 0
for i in range(n):
    s = input()
    if s.count('11') >= 3:
        counter += 1
print(counter)


# На вход программе подается строка генетического кода, состоящая из букв А (аденин), Г (гуанин), Ц (цитозин), Т (тимин).
# Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и тимина входит в данную строку генетического кода.
# Формат входных данных: На вход программе подается строка генетического кода, состоящая из символов А, Г, Ц, Т, а, г, ц, т.
# Формат выходных данных: Программа должна вывести сколько гуанина, тимина, цитозина, аденина входит в данную строку генетического кода.
# Примечание. Строка не содержит символов, кроме как А, Г, Ц, Т, а, г, ц, т.
s = input()
s = s.lower()
print('Аденин:', s.count('а'))
print('Гуанин:', s.count('г'))
print('Цитозин:', s.count('ц'))
print('Тимин:', s.count('т'))


# На вход программе подается строка текста, состоящая из слов, разделенных ровно одним пробелом. Напишите программу, которая подсчитывает
# количество слов в ней.
# Формат входных данных: На вход программе подается строка текста.
# Формат выходных данных: Программа должна вывести количество слов.
# Примечание 1. Строка текста не содержит пробелов в начале и конце.
# Примечание 2. Используйте для решения задачи метод count.
s = input()
print(s.count(' ') + 1)

# На вход программе подается строка. Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
# Формат входных данных: На вход программе подается строка.
# Формат выходных данных: Программа должна вывести количество буквенных символов в нижнем регистре.
s = input()
counter = 0
for i in range(len(s)):
    if s[i] in 'qwertyuiopasdfghjklzxcvbnm':
        counter += 1
print(counter)


# На вход программе подается строка текста. Напишите программу, которая определяет является ли оттенок текста хорошим или нет.
# Текст имеет хороший оттенок, если содержит подстроку «хорош» во всевозможных регистрах.
# Формат входных данных: На вход программе подается строка текста.
# Формат выходных данных: Программа должна вывести «YES» если текст имеет хороший оттенок и «NO» в противном случае.
# Примечание. Текст содержащий хорош, ХОРОШ, Хорош, хОРОШ и т.д. имеет хороший оттенок.
s = input()
if 'хорош' in s.lower():
    print('YES')
else:
    print('NO')


# На вход программе подается строка. Напишите программу, которая меняет регистр символов, другими словами замените все
# строчные символы заглавными и наоборот.
# Формат входных данных: На вход программе подается строка.
# Формат выходных данных: Программа должна вывести строку в соответствии с условием задачи.
s = input()
print(s.swapcase())


# На вход программе подается строка состоящая из имени и фамилии человека, разделенных одним пробелом. Напишите программу,
# которая проверяет, что имя и фамилия начинаются с заглавной буквы.
# Формат входных данных: На вход программе подается строка.
# Формат выходных данных: Программа должна вывести «YES» если имя и фамилия начинаются с заглавной буквы и «NO» в противном случае.
# Примечание. Строка содержит только буквы.
s = input()
if s == s.title():
    print('YES')
else:
    print('NO')
 

# На вход программе подается строка текста. Напишите программу, которая разрежет ее на две равные части, переставит их местами
# и выведет на экран.
# Формат входных данных: На вход программе подается строка текста.
# Формат выходных данных: Программа должна вывести текст в соответствии с условием задачи.
# Примечание. Если длина строки нечетная, то длина первой части должна быть на один символ больше.
s = input()
if len(s) % 2 != 0:
    half = (len(s) // 2) + 1
    print(s[half:] + s[:half])
else:
    half = len(s) // 2
    print(s[half:] + s[:half])



# На вход программе подается одна строка. Напишите программу, которая выводит:
# третий символ этой строки;
# предпоследний символ этой строки;
# первые пять символов этой строки;
# всю строку, кроме последних двух символов;
# все символы с четными индексами;
# все символы с нечетными индексами;
# все символы в обратном порядке;
# все символы строки через один в обратном порядке, начиная с последнего.
# Формат входных данных: На вход программе подается одна строка, длина которой больше 5 символов.
# Формат выходных данных: Программа должна вывести данные в соответствии с условием. Каждое значение выводится на отдельной строке.
s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])


# На вход программе подается одна строка. Напишите программу, которая выводит:
# общее количество символов в строке;
# исходную строку повторенную 3 раза;
# первый символ строки;
# первые три символа строки;
# последние три символа строки;
# строку в обратном порядке;
# строку с удаленным первым и последним символом.
# Формат входных данных: На вход программе подается одна строка, длина которой больше 3 символов.
# Формат выходных данных: Программа должна вывести данные в соответствии с условием. Каждое значение выводится на отдельной строке.
s = input()
print(len(s))
print(s * 3)
print(s[0])
print(s[:3])
print(s[-3:])
print(s[::-1])
print(s[1:-1])


# На вход программе подается одно слово, записанное в нижнем регистре. Напишите программу, которая определяет является ли оно палиндромом.
# Формат входных данных: На вход программе подается одно слово в нижнем регистре.
# Формат выходных данных: Программа должна вывести «YES», если слово является палиндромом и «NO» в противном случае.
# Примечание. Палиндром читается одинаково в обоих направлениях, например слово «потоп».
s = input()
if s == s[::-1]:
    print('YES')
else:
    print('NO')


# На вход программе подается натуральное число, записанное в десятичной системе счисления. Напишите программу,
# которая переводит данное число в двоичную систему счисления.
# Формат входных данных: На вход программе подается одно натуральное число.
# Формат выходных данных: Программа должна вывести число записанное в двоичной системе счисления.
n = int(input())
bi = str()
while n != 0:
    y = int(n % 2)
    n = int(n / 2)
    bi = str(y) + bi
print(bi)


# На вход программе подается одна строка с буквами русского языка. Напишите программу, которая определяет количество гласных
# и согласных букв.
# Формат входных данных: На вход программе подается одна строка.
# Формат выходных данных: Программа должна вывести количество гласных и согласных букв.
# Примечание. В русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е)
# и 21 согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).
s = input()
vowels = 0
consonats = 0
for i in range(len(s)):
    if s[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        vowels += 1
    if s[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        consonats += 1
print('Количество гласных букв равно', vowels)
print('Количество согласных букв равно', consonats)

# На вход программе подается одна строка. Напишите программу, которая определяет сколько в ней одинаковых соседних символов.
# Формат входных данных: На вход программе подается одна строка.
# Формат выходных данных: Программа должна вывести количество одинаковых соседних символов.
a = input()
counter = 0
for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        counter += 1
print(counter)


# На вход программе подается одна строка. Напишите программу, которая определяет сколько раз в строке встречаются символы + и *.
# Формат входных данных: На вход программе подается одна строка.
# Формат выходных данных: Программа должна вывести сколько раз встречаются символы  + и * в строке.
a = input()
plus = 0
star = 0
for i in range(len(a)):
    if '+' in a[i]:
        plus += 1
    if '*' in a[i]:
        star += 1
print('Символ + встречается', plus, 'раз')
print('Символ * встречается', star, 'раз')


# На вход программе подается одна строка. Напишите программу, которая выводит сообщение «Цифра» (без кавычек),
# если строка содержит цифру. В противном случае вывести сообщение «Цифр нет» (без кавычек).
# Формат входных данных: На вход программе подается одна строка.
# Формат выходных данных: Программа должна вывести текст в соответствии с условием задачи.
a = input()
if '0' in a or '1' in a or '2' in a or '3' in a or '4' in a or '5' in a or '6' in a or '7' in a or '8' in a or '9' in a:
    print('Цифра')
else:
    print('Цифр нет')


# На вход программе подается одна строка состоящая из цифр. Напишите программу, которая считает сумму цифр данной строки.
# Формат входных данных: На вход программе подается одна строка состоящая из цифр.
# Формат выходных данных: Программа должна вывести сумму цифр данной строки.
n = int(input())
summa = 0
while n > 0:
    last_digit = n % 10
    summa += last_digit
    n = n // 10
print(summa)


# На вход программе подаются три строки: имя, фамилия и отчество. Напишите программу, которая выводит инициалы человека.
# Формат входных данных: На вход программе подаются три строки, каждая на отдельной строке.
# Формат выходных данных: Программа должна вывести ФИО человека.
# Примечание. Гарантируется, что имя, фамилия и отчество начинаются с заглавной буквы.
name = input()
surname = input()
patronymic = input()
print( surname[0], name[0], patronymic[0], sep='')


# На вход программе подается одна строка. Напишите программу, которая выводит в столбик элементы строки в обратном порядке.
# Формат входных данных: На вход программе подается одна строка.
# Формат выходных данных: Программа должна вывести в столбик элементы строки в обратном порядке. 
a = str(input())
for c in range(1, len(a) + 1):
    print(a[-c])


# На вход программе подается одна строка. Напишите программу, которая выводит элементы строки с индексами 0, 2, 4, ... в столбик.
# Формат входных данных: На вход программе подается одна строка.
# Формат выходных данных: Программа должна вывести элементы строки с индексами 0, 2, 4, ..., каждое на отдельной строке.
string = str(input())
for i in range(0, len(string), 2):
    print(string[i])

