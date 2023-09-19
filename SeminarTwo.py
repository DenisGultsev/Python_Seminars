# for (int i = 0; i <= 5; i++) i = i + 1 <-> i += 1
# ++i <-> i++

# for element in True, False, 2, 1.345, "Hello, world!":
#     print(element * 2)

# for i in range(5):
#     print(i)

# print(*range(5))
# range(begin = 0, end = обязательно, step = + 1)
# print(*range(2, 7, 2))
# print(*range(12, 1, -3))
# print(*range(12, -1, -3))

# n = 10
# while n > 0:

#     print(n, end=' ')
# n -= 2

# task 9

# n = int(input())
# result = 1

# while n > 0:
#     result *= n
#     n -= 1

# print(result)

# task 11

# def fibonacci_number(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         prev = 0
#         curr = 1
#         count = 2
#         while curr < n:
#             temp = curr
#             curr = curr + prev
#             prev = temp
#             count += 1
#         if curr == n:
#             return count
#         else:
#             return -1


# A = int(input("Введите число A: "))
# result = fibonacci_number(A)
# print()
# print(result)

# task 15

N = int(input("Введите количество арбузов: "))
weights = []

for i in range(N):
    weight = int(input(f"Введите массу {i+1} арбуза: "))
    weights.append(weight)

min_weight = min(weights)
max_weight = max(weights)

print()
print(f"Самый легкий арбуз: {min_weight}")
print(f"Самый тяжелый арбуз: {max_weight}")
