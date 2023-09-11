# C#/C++/C/Java - статическая типизация данных
# Python/JavaScript - динамическая типизация данных

# int age = 27; -> []

# age = 27 -> class 'int' -> []

# Компилятор и Интерпритатор

# name = input("Введите свое имя: ")
# print(f'Hello, {name}!')
# print(type(name))

# Базовые функции:

# str() int() float()
# C#(int) <= |2147000000|

# age = int(input("Введите ваш возвраст: "))
# print(f'Ваш возвраст {age}')

# dlina = float(input("Введите длину стопы: "))
# print(int(dlina))

# print(124 + 'Den')
# print(str(124) + 'Den')

# n = 5
# m = 2
# print(n // m)  # выводит целую часть
# print(n / m)  # выводит целую и дробные части
# print(n % m)  # выводит остаток от числа
# print(n ** m)

# print(5 > 7)  # False
# print(5 < 9)  # True

# print(int(5 > 7))  # False
# print(int(5 < 9))  # True

# &&(and) - конъюкция(логическое умножение)
# ||(or) - дизъюнкция(логическое сложение)
# !(not) - отрицание(противоположное значение)

# if not False:
#     print(1)

# n = int(input("Введите число: "))
# if n > 7 and n < 11 or n > 100:
#     print('yes')
# else:
#     print('no')

# Задача № 1.
# За день машина проезжает n километров. Сколько дней нужно,
# чтобы проехать по маршруту длиной m километров?
# При выполнении этой задачи нельзя пользоваться
# условной инструкцией if и циклами.

# import math

# n = 700
# m = 700

# days = math.ceil(m / n)

# print(days)

# Задача № 2.
# В какой-то школе решили взять три новых математических класса
# и оборудовать кабинеты для них новыми партами.
# За каждой партой могут сидеть два ученика.
# Известно количество учащихся в каждом из трех классов.
# Вы вводите меньшее количество деталей, которые необходимо приобрести для них.

# import math

# students_class1 = int(input("Введите количество парт в классе 1: "))
# students_class2 = int(input("Введите количество парт в классе 2: "))
# students_class3 = int(input("Введите количество парт в классе 3: "))

# desks_class1 = math.ceil(students_class1 / 2)
# desks_class2 = math.ceil(students_class2 / 2)
# desks_class3 = math.ceil(students_class3 / 2)

# total_desks = desks_class1 + desks_class2 + desks_class3

# print(total_desks)
