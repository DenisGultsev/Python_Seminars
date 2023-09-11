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

import math

n = 700
m = 700

days = math.ceil(m / n)

print(days)
