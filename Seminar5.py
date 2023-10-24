# Факториал числа n

# def factorial(n):
#     if n < 0:
#         return "Факториал определен только для неотрицательных чисел"
#     elif n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)


# n = int(input("Введите число: "))
# print(factorial(n))

# Сумма факториалов

# def summa(n):
#     if n == 1:
#         return 1
#     else:
#         return n + summa(n-1)


# n = int(input("Введите число: "))
# print(summa(n))

# Номер числа Фибоначчи

# from datetime import datetime


# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# n = int(input("Введите число N: "))
# start_time = datetime.now()
# result = fibonacci(n)
# print(result)
# end_time = datetime.now()
# print(f'Время работы алгоритма через рекурсию {end_time - start_time}')

# start_time = datetime.now()
# a0, a1 = 0, 1
# for i in range(n):
#     next_n = a0 + a1
#     a0 = a1
#     a1 = next_n
# print(a0)
# end_time = datetime.now()
# print(f'Время работы алгоритма линейной программы {end_time - start_time}')

# Оценки

# n = int(input("Введите количество оценок: "))
# marks = [int(i) for i in input("Введите оценки: ").split()][:n]
# print(*[min(marks) if max(marks) == j else j for j in marks])

# Простое число

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


number = int(input("Введите число: "))
if is_prime(number):
    print("Да, число является простым.")
else:
    print("Нет, число не является простым.")
