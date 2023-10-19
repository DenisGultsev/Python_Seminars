# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата `_n`.

# **Input:** a a a b c a a d c d d
# **Output:** a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию `.split()`.

# def track_character_repeats(input_string):
#     symbols = input_string.split()
#     replays = {}
#     result = []

#     for symbol in symbols:
#         if symbol not in replays:
#             replays[symbol] = 1
#             result.append(symbol)
#         else:
#             replays[symbol] += 1
#             result.append(f"{symbol}_{replays[symbol]}")

#     return ' '.join(result)


# input_string = "f f a s a f q a q s d"
# output_string = track_character_repeats(input_string)
# print(output_string)

# Пользователь вводит текст(строка). Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов. Определите, сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells that she sells are sea shells
# I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13

# text = input("Введите текст: ")  # просим пользователя ввести текст

# # разбиваем текст на слова и приводим их к нижнему регистру
# words = text.lower().split()

# # создаем множество для хранения уникальных слов
# unique_words = set(words)

# # выводим количество различных слов
# print("Количество различных слов:", len(unique_words))

# Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)

subsequence = [1, 5, 0, 3, 7, 9, 2]
maximum_value = subsequence[0]

for number in subsequence:
    if number == 0:
        break
    if number > maximum_value:
        maximum_value = number

print(maximum_value)
