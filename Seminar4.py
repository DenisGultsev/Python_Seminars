# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата `_n`.

# **Input:** a a a b c a a d c d d
# **Output:** a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию `.split()`.


def track_character_repeats(input_string):
    symbols = input_string.split()
    replays = {}
    result = []

    for symbol in symbols:
        if symbol not in replays:
            replays[symbol] = 1
            result.append(symbol)
        else:
            replays[symbol] += 1
            result.append(f"{symbol}_{replays[symbol]}")

    return ' '.join(result)


input_string = "f f a s a f q a q s d"
output_string = track_character_repeats(input_string)
print(output_string)
