"""Задания к главе 3.4.

"Встроенные возможности по работе с коллекциями".

Хендбук Яндекс "Основы Python".
"""

# A

# +
from itertools import (
    accumulate,
    chain,
    combinations,
    count,
    cycle,
    permutations,
    product,
)

items_list = input().split()

for index, item in enumerate(items_list):
    print(f"{index + 1}. {item}")
# -

# B

# +
colunm1 = input().split(", ")
colunm2 = input().split(", ")

for child1, child2 in zip(colunm1, colunm2):
    print(f"{child1} - {child2}")
# -

# C

# +
nums = list(map(float, input().split()))

for num in count(nums[0], nums[2]):
    rounded = round(num, 2)

    if rounded > nums[1]:
        break

    print(rounded)
# -

# D

# +
words = input().split()

for word in accumulate(map(lambda x: " " + x, words)):
    print(word[1:])
# -

# E

# +
list1 = input().split(", ")
list2 = input().split(", ")
list3 = input().split(", ")


main_list = sorted(chain(list1, list2, list3))

for index, item in enumerate(main_list):
    print(f"{index + 1}. {item}")
# -

# F

# +
suits_f = ["пик", "треф", "бубен", "червей"]
weights_f = [2, 3, 4, 5, 6, 7, 8, 9, 10, "валет", "дама", "король", "туз"]

suit_to_exclude = input()

suits_f.remove(suit_to_exclude)

for weight, suit in product(weights_f, suits_f):
    print(weight, suit)
# -

# G

# +
students = [input() for _ in range(int(input()))]

for student1, student2 in combinations(students, r=2):
    print(f"{student1} - {student2}")
# -

# H

# +
porridges = [input() for _ in range(int(input()))]
days_amount = int(input())

counter = 1

for porridge in cycle(porridges):
    if counter > days_amount:
        break

    print(porridge)
    counter += 1
# -

# I

# +
size = int(input())

table = [x * y for x, y in product(range(1, size + 1), repeat=2)]

for index in range(0, size * size):
    end = " " if (index + 1) % size != 0 else "\n"

    print(table[index], end=end)
# -

# J

# +
slices = int(input())

print("А Б В")

for value1, value2 in product(range(1, slices), repeat=2):
    value3 = slices - value1 - value2

    if value3 > 0:
        print(value1, value2, value3)
# -

# K

# +
height_k = int(input())
width_k = int(input())

max_length = len(str(height_k * width_k))

for row, column in product(range(1, height_k + 1), range(1, width_k + 1)):
    print(f"{column + width_k * (row - 1):>{max_length}}", end=" ")

    if column == width_k:
        print()
# -

# L

# +
products_list = []

for _ in range(int(input())):
    products_list.append(input().split(", "))

for index, value in enumerate(sorted(chain.from_iterable(products_list))):
    print(f"{index + 1}. {value}")
# -

# M

# +
athlete_list = []

for _ in range(int(input())):
    athlete_list.append(input())

athlete_list.sort()

for combination in permutations(athlete_list, len(athlete_list)):
    print(", ".join(combination))
# -

# N

# +
winners_list = []

for _ in range(int(input())):
    winners_list.append(input())

winners_permutations = permutations(sorted(winners_list), r=3)

for winners in winners_permutations:
    print(", ".join(winners))
# -

# O

# +
purchases_list = []

for _ in range(int(input())):
    purchases_list.extend(input().split(", "))


purchases_list.sort()

purchases_permutations = permutations(purchases_list, r=3)

for purchases in purchases_permutations:
    print(" ".join(purchases))
# -

# P

# +
suits: list[str] = ["бубен", "пик", "треф", "червей"]
weights: list[str] = [
    "10",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "валет",
    "дама",
    "король",
    "туз",
]

suits_dict: dict[str, str] = {
    "буби": "бубен",
    "пики": "пик",
    "трефы": "треф",
    "черви": "червей",
}

required_suit = input()
weight_to_exclude = input()

weights.remove(weight_to_exclude)

card_products = product(weights, suits)

card_combinations = combinations(card_products, r=3)

counter = 0


for combination_p in card_combinations:
    if counter >= 10:
        break

    current = ", ".join(map(" ".join, chain(combination_p)))

    if suits_dict[required_suit] not in current:
        continue

    print(current)

    counter += 1
# -

# Q

# +
suits_q: list[str] = ["бубен", "пик", "треф", "червей"]
weights_q: list[str] = [
    "10",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "валет",
    "дама",
    "король",
    "туз",
]

suits_dict_q: dict[str, str] = {
    "буби": "бубен",
    "пики": "пик",
    "трефы": "треф",
    "черви": "червей",
}

required_suit = input()
weight_to_exclude = input()
previous = input()

weights_q.remove(weight_to_exclude)

card_products = product(weights_q, suits_q)

card_combinations_q = combinations(card_products, r=3)

is_last = False

for combination_q in card_combinations_q:

    current = ", ".join(map(" ".join, chain(combination_q)))

    if suits_dict_q[required_suit] not in current:
        continue

    if is_last:
        print(current)
        break

    if current == previous:
        is_last = True
# -

# R

# +
values_list_r: list[int] = [0, 1]

triples = product(values_list_r, repeat=3)

expression = input()

# Из-за того, что линтер не разрешает имена вида a, b, c
# заменим все однобуквенные имена на более длинные
expression_list = expression.split()

for index, word in enumerate(expression_list):
    match word:
        case "a":
            expression_list[index] = "a_value"
        case "b":
            expression_list[index] = "b_value"
        case "c":
            expression_list[index] = "c_value"

expression = " ".join(expression_list)

print("a b c f")

for triple in triples:
    a_value, b_value, c_value = triple

    # pylint: disable=eval-used
    result = int(eval(expression))

    print(a_value, b_value, c_value, result)
# -

# S

# +
upper_letters = [chr(i) for i in range(ord("A"), ord("Z") + 1)]

expression = input()

count_uppers = len({word for word in expression.split() if word.isupper()})

values_list: list[str] = ["0", "1"]

digit_sets = product(values_list, repeat=count_uppers)

print(" ".join(upper_letters[:count_uppers]), "F")

for digit_set in digit_sets:
    current = expression

    for index, value in enumerate(digit_set):
        current = current.replace(upper_letters[index], value)

    # Условие задачи требует использовать eval
    # pylint: disable=eval-used
    result = int(eval(current))

    print(" ".join(list(digit_set)), result)
# -

# T
