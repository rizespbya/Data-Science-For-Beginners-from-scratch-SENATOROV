"""Задания к главе 3.3.

"Списочные выражения. Модель памяти для типов языка Python".

Хендбук Яндекс "Основы Python".
"""

# A

start_a = int(input())
start_b = int(input())
result = [num**2 for num in range(start_a, start_b + 1)]

# B

start_a = int(input())
finish_b = int(input())
result_b = [
    number**2
    for number in range(
        start_a,
        finish_b + 1 if start_a < finish_b else finish_b - 1,
        1 if start_a < finish_b else -1,
    )
]

# C

# +
start_c = int(input())
finish_c = int(input())
divider_c = int(input())

range_c = range(start_c, finish_c + 1)

result_c = [num for num in range_c if num % divider_c == 0]
# -

# D

# +
numbers_d = [1, 2, 3, 4, 5]

result_d = {num for num in numbers_d if num % 2 == 1}
# -

# E

# +
numbers_e = [1, 2, 3, 4, 5]

result_e = {num for num in numbers_e if num**0.5 // 1 == num**0.5}
# -

# F

# +
sentence = "Мама мыла раму"

result_f = [len(x) for x in sentence.split()]
# -

# G

# +
text = "2 + 2 = 4"

"".join([char for char in text if char.isdigit()])
# -

# H

# +
string = "Российская Федерация"

"".join([word[0].upper() for word in string.split()])
# -

# I

# +
numbers_i = [3, 1, 2, 3, 2, 2, 1]

" - ".join(map(str, sorted(set(numbers_i))))
# -

# J

# +
words_j = "Ехали медведи на велосипеде"

vowels = "аяуюоёэеиыaeiouy"


def is_valid(word: str) -> bool:
    """Функция для проверки количества гласных в слове.

    Args:
        word (str): слово для проверки

    Returns:
        bool: True, если гласных 3 или больше. Иначе False
    """
    return len([letter for letter in word if letter.lower() in vowels]) >= 3


result_j = [word for word in words_j.split() if is_valid(word)]
# -

# K

# +
numbers_k = [1, 2, 1, 3, 1, 2, 2, 4, 1, 2, 5, 1, 2]

result_k = {num for num in numbers_k if numbers_k.count(num) == 1}
# -

# L

# +
numbers_l = {2, 4, 5, 7, -10, -8, 10, -9, -1}

max({num1 * num2 for num1 in numbers_l for num2 in numbers_l if num1 != num2})
# -

# M

# +
data_m = {"a": [1, 2, 3], "b": [2, 3, 4, 5]}

result_m = min((sum(nums), letter) for letter, nums in data_m.items())[1]
# -

# N

# +
data_n = {"a": [1, 2, 1], "b": [2, 3, 2, 5, 1]}

items_n = data_n.items()

result_n = {letter for letter, nums in items_n if len(nums) != len(set(nums))}
# -

# O

# +
text_o = "Мама мыла раму!"

result_o = {
    letter: text_o.lower().count(letter)
    for letter in text_o.lower()
    if letter.isalpha()
}
# -

# P

# +
rle = [("a", 2), ("b", 3), ("c", 1)]

"".join(letter * count for letter, count in rle)
# -

# Q

# +
num_q = 3

range_q = range(1, num_q + 1)

result_q = [[column * row for column in range_q] for row in range_q]
# -

# R

# +
numbers_r = {1, 2, 3, 4, 5}

result_r = {
    num: [divider for divider in range(1, num + 1) if num % divider == 0]
    for num in numbers_r
}
# -

# S

# +
numbers_s = {1, 2, 3, 4, 5}


def is_prime(num: int) -> bool:
    """Функция для проверки простого числа.

    Args:
        num (int): слово для проверки

    Returns:
        bool: True, если число простое. Иначе False
    """
    if num <= 1:
        return False

    dividers_range = range(2, int(num**0.5 + 1))

    return len([div for div in dividers_range if not num % div]) == 0


result_s = {num for num in numbers_s if is_prime(num)}
# -

# T

# +
text_t = "ехали медведи на велосипеде"

result_t = {
    tuple(sorted([word1, word2]))
    for word1 in text_t.split()
    for word2 in text_t.split()
    if word1 != word2 and len(set(word1) & set(word2)) >= 3
}
