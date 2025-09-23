"""Задания к главе 3.2 "Множества, словари".

Хендбук Яндекс "Основы Python".
"""

# A

# +
from typing import TypedDict

print("".join(set(input())))
# -

# B

print("".join(set(input()) & set(input())))

# C

# +
my_set: set[str] = set()

for _ in range(int(input())):
    items = input().split()

    for item in items:
        my_set.add(item)

for item in my_set:
    print(item)
# -

# D

# +
semolina_porridge: set[str] = set()
oatmeal: set[str] = set()

semolina_amount = int(input())
oatmeal_amount = int(input())

for _ in range(semolina_amount):
    semolina_porridge.add(input())

for _ in range(oatmeal_amount):
    oatmeal.add(input())

print(len(semolina_porridge ^ oatmeal) or "Таких нет")
# -

# E

# +
semolina_amount = int(input())
oatmeal_amount = int(input())

child_names: list[str] = []

for _ in range(semolina_amount + oatmeal_amount):
    child_names.append(input())

filtered = filter(lambda name: child_names.count(name) == 1, child_names)

print(len(list(filtered)) or "Таких нет")
# -

# F

# +
semolina_amount = int(input())
oatmeal_amount = int(input())

names: list[str] = []

for _ in range(semolina_amount + oatmeal_amount):
    names.append(input())

filtered = filter(lambda name: names.count(name) == 1, names)

names_list = sorted(list(filtered))

print("\n".join(names_list) if len(names_list) != 0 else "Таких нет")
# -

# G

# +
MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}

words = input().upper().split()

coded_words = [" ".join(map(lambda char: MORSE[char], list(w))) for w in words]

print("\n".join(coded_words))
# -

# H

# +
porridge_dict: dict[str, list[str]] = {}

for _ in range(int(input())):
    input_list = input().split()
    name = input_list[0]

    for porridge in input_list[1::]:
        if porridge not in porridge_dict:
            porridge_dict[porridge] = []
        porridge_dict[porridge].append(name)


target_porridge = input()

if target_porridge in porridge_dict:
    names_list = sorted(porridge_dict[target_porridge])
    print("\n".join(names_list))
else:
    print("Таких нет")
# -

# I

# +
lands_dict: dict[str, int] = {}

while land := input():
    for word in land.split():
        if word not in lands_dict:
            lands_dict[word] = 0
        lands_dict[word] = (lands_dict[word] or 0) + 1


for key, value in lands_dict.items():
    print(key, value)
# -

# J

# +
LETTERS: dict[str, str] = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "ZH",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "KH",
    "Ц": "TC",
    "Ч": "CH",
    "Ш": "SH",
    "Щ": "SHCH",
    "Ы": "Y",
    "Э": "E",
    "Ю": "IU",
    "Я": "IA",
    "Ь": "",
    "Ъ": "",
}


input_str = input()

for char in input_str:
    if char.upper() not in LETTERS:
        print(char, end="")
    else:
        is_upper = char.isupper()
        translit = LETTERS[char.upper()]

        display_value = translit.capitalize() if is_upper else translit.lower()

        print(display_value, end="")
# -

# K

# +
names_dict: dict[str, int] = {}

for _ in range(int(input())):
    name = input()

    if name in names_dict:
        names_dict[name] += 1
    else:
        names_dict[name] = 1

print(sum(filter(lambda value: value > 1, names_dict.values())))
# -

# L

# +
names_dict_l: dict[str, int] = {}

for _ in range(int(input())):
    name = input()

    if name in names_dict_l:
        names_dict_l[name] += 1
    else:
        names_dict_l[name] = 1

pairs = list(filter(lambda item: item[1] > 1, names_dict_l.items()))

pairs.sort(key=lambda pair: pair[0])

if len(pairs) != 0:
    for name, counter in pairs:
        print(name, "-", counter)
else:
    print("Однофамильцев нет")
# -

# M

# +
dishes_amount = int(input())

dishes = {input() for _ in range(dishes_amount)}


not_allowed_dishes = set()

for _ in range(int(input())):
    for _ in range(int(input())):
        not_allowed_dishes.add(input())


allowed_dishes = sorted(list(dishes - not_allowed_dishes))

result = "\n".join(allowed_dishes)

print(result or "Готовить нечего")
# -

# N

# +
ingredients = {input() for _ in range(int(input()))}


cookbook: dict[str, set[str]] = {}

for _ in range(int(input())):
    dish = input()
    cookbook[dish] = set()

    for _ in range(int(input())):
        cookbook[dish].add(input())


allowed_dishes_n: list[str] = []

for dish, ingredients_list in cookbook.items():
    if ingredients >= ingredients_list:
        allowed_dishes_n.append(dish)


sorted_dishes = sorted(allowed_dishes_n)

print("\n".join(sorted_dishes) if sorted_dishes else "Готовить нечего")


# -

# O


# +
class NumberStats(TypedDict):
    """Статистика числа, содержащая информацию о составе цифр.

    Attributes:
        digits (int): Общее количество цифр в числе
        units (int): Количество единиц в числе
        zeros (int): Количество нулей в числе
    """

    digits: int
    units: int
    zeros: int


statistics: list[NumberStats] = []

for number in input().split():
    bin_number = f"{int(number):b}"

    statistics.append(
        {
            "digits": len(bin_number),
            "units": bin_number.count("1"),
            "zeros": bin_number.count("0"),
        }
    )


print(statistics)
# -

# P

# +
items_set: set[str] = set()

while land := input():
    items_list = land.split()

    for index, item in enumerate(items_list):
        if item == "зайка":
            if index > 0:
                items_set.add(items_list[index - 1])
            if index < len(items_list) - 1:
                items_set.add(items_list[index + 1])

for item in items_set:
    print(item)


# -

# Q


# +
class Person(TypedDict):
    """Информация о друзьях первой и второй линии.

    Attributes:
        first_line set[str]: Друзья первой линии
        second_line set[str]: Друзья второй линии
    """

    first_line: set[str]
    second_line: set[str]


friends: dict[str, Person] = {}


def create_person(person_name: str) -> None:
    """Добавляет имя в словарь friends, если имя в словаре отсутствует.

    Args:
        name (str): добавляемое имя
    """
    if person_name not in friends:
        new_person: Person = {"first_line": set(), "second_line": set()}
        friends[person_name] = new_person


while names := input().split():
    person, friend = names

    create_person(person)

    friends[person]["first_line"].add(friend)

    create_person(friend)

    friends[friend]["first_line"].add(person)

for name, friends_dict in friends.items():
    nearest_friends = friends_dict["first_line"]

    for nearest_friend in nearest_friends:

        first_line = friends[nearest_friend]["first_line"]
        second_line = friends[nearest_friend]["second_line"]
        added_friends = second_line | nearest_friends - first_line
        added_friends.discard(nearest_friend)

        friends[nearest_friend]["second_line"] = added_friends


for name in sorted(friends.keys()):
    print(f"{name}: {', '.join(sorted(friends[name]['second_line']))}")
# -

# S

# +
toys: list[str] = []

for _ in range(int(input())):
    child_toys = set(input().split(": ")[1].split(", "))

    toys.extend(child_toys)


all_toys: set[str] = set()
unique: set[str] = set()

for toy in toys:
    if toy not in all_toys:
        all_toys.add(toy)
        unique.add(toy)
    else:
        unique.discard(toy)

for toy in sorted(unique):
    print(toy)
