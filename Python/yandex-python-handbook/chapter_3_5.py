"""Задания к главе 3.5.

Потоковый ввод/вывод. Работа с текстовыми файлами. JSON.

Хендбук Яндекс "Основы Python".
"""

# A

# +
import json
import math
from itertools import chain
from sys import stdin

sum_a = sum(map(int, stdin.read().split()))

print(sum_a)
# -

# B

# +
children = list(map(lambda line: line.rstrip("\n").split(), stdin.readlines()))

total_diff = sum(map(lambda child: int(child[2]) - int(child[1]), children))

print(round(total_diff / len(children)))
# -

# C

# +
code_lines = map(lambda line: line.rstrip("\n"), stdin.readlines())

for code_line in code_lines:
    hash_index = code_line.find("#")

    match (hash_index):
        case -1:
            print(code_line)
        case 0:
            continue
        case _:
            print(code_line[:hash_index])
# -

# D

# +
input_d = stdin.readlines()
titles = input_d[:-1]
search_request = input_d[-1].rstrip("\n").lower()


for title in titles:
    if search_request in title.lower():
        print(title.rstrip("\n"))
# -

# E

# +
input_words: list[str] = []

for words in stdin:
    input_words.extend(words.rstrip("\n").split())

palindromes = list({word for word in input_words if word.lower() == word[::-1].lower()})

palindromes.sort()

print("\n".join(palindromes))
# -

# F

# +
# _буква добавлена для того, чтобы избежать дублирования кода
# и как следствие ошибок pylint
LETTERS: dict[str, str] = {
    "А_буква": "A",
    "Б_буква": "B",
    "В_буква": "V",
    "Г_буква": "G",
    "Д_буква": "D",
    "Е_буква": "E",
    "Ё_буква": "E",
    "Ж_буква": "Zh",
    "З_буква": "Z",
    "И_буква": "I",
    "Й_буква": "I",
    "К_буква": "K",
    "Л_буква": "L",
    "М_буква": "M",
    "Н_буква": "N",
    "О_буква": "O",
    "П_буква": "P",
    "Р_буква": "R",
    "С_буква": "S",
    "Т_буква": "T",
    "У_буква": "U",
    "Ф_буква": "F",
    "Х_буква": "Kh",
    "Ц_буква": "Tc",
    "Ч_буква": "Ch",
    "Ш_буква": "Sh",
    "Щ_буква": "Shch",
    "Ы_буква": "Y",
    "Э_буква": "E",
    "Ю_буква": "Iu",
    "Я_буква": "Ia",
    "Ь_буква": "",
    "Ъ_буква": "",
}

with open("cyrillic.txt", encoding="utf-8") as my_file:
    text = my_file.read()

transformed_text = ""

for letter in text:
    upper_letter = letter.upper()

    key = f"{upper_letter}_буква"

    if key not in LETTERS:
        transformed_text += letter
        continue

    is_upper = letter.isupper()

    transformed_text += LETTERS[key] if is_upper else LETTERS[key].lower()


with open("transliteration.txt", "w", encoding="UTF-8") as file_out:
    file_out.write(transformed_text)
# -

# G

# +
file_name = input()

with open(file_name, encoding="utf-8") as my_file:
    nums_iter = chain(*[line.rstrip("/n").split() for line in my_file.readlines()])

    numbers = [int(num) for num in nums_iter]

print(len(numbers))
print(len([num for num in numbers if num > 0]))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(round(sum(numbers) / len(numbers), 2))
# -

# H

# +
file1 = input()
file2 = input()
file3 = input()

set1: set[str] = set()
set2: set[str] = set()

with open(file1, encoding="utf-8") as current_file:
    set1 = {word for word in current_file.read().split()}

with open(file2, encoding="utf-8") as current_file:
    set2 = {word for word in current_file.read().split()}


with open(file3, "w", encoding="utf-8") as file_out:
    file_out.write("\n".join(sorted(set1.symmetric_difference(set2))))
# -

# I

# +
file_in_i = input()
file_out_i = input()

result: list[list[str]] = []

with open(file_in_i, encoding="utf-8") as file:
    for line in file:
        result.append(line.strip().replace("\t", "").split())


with open(file_out_i, "w", encoding="utf-8") as file:
    file.writelines([" ".join(line) + "\n" for line in result if line])
# -

# J

# +
file_name = input()
lines_amount = int(input())

with open(file_name, encoding="utf-8") as file:
    display_lines = file.readlines()[-lines_amount:]
    print("".join(display_lines))
# -

# K

# +
file_in = input()
file_out_k = input()

with open(file_in, encoding="utf-8") as my_file:
    nums = chain(*[line.rstrip("/n").split() for line in my_file.readlines()])
    numbers = [int(num) for num in nums]


statistic: dict[str, int | float] = {
    "count": len(numbers),
    "positive_count": len([num for num in numbers if num > 0]),
    "min": min(numbers),
    "max": max(numbers),
    "sum": sum(numbers),
    "average": round(sum(numbers) / len(numbers), 2),
}

with open(file_out_k, "w", encoding="UTF-8") as my_file:
    json.dump(statistic, my_file, ensure_ascii=False, indent=2)
# -

# L

# +
file_1 = input()
file_2 = input()
file_3 = input()
file_4 = input()

evens: list[str] = []
odds: list[str] = []
equals: list[str] = []

even_digits = "02468"
odd_digits = "13579"

with open(file_1, encoding="utf-8") as my_file:
    nums_lines = my_file.readlines()

    for line in nums_lines:

        temp_evens: list[str] = []
        temp_odds: list[str] = []
        temp_equals: list[str] = []

        for number in line.split():
            evens_count = len([i for i in number if i in even_digits])
            odd_count = len([i for i in number if i in odd_digits])

            if evens_count > odd_count:
                temp_evens.append(number)
            elif evens_count < odd_count:
                temp_odds.append(number)
            else:
                temp_equals.append(number)

        evens.append(" ".join(temp_evens) + "\n")
        odds.append(" ".join(temp_odds) + "\n")
        equals.append(" ".join(temp_equals) + "\n")

    with open(file_2, "w", encoding="UTF-8") as file:
        file.writelines(evens)
    with open(file_3, "w", encoding="UTF-8") as file:
        file.writelines(odds)
    with open(file_4, "w", encoding="UTF-8") as file:
        file.writelines(equals)
# -

# M

# +
file_name = input()

result_m: dict[str, str]

with open(file_name, encoding="utf-8") as file:
    result_m = json.load(file)

for line in stdin.readlines():

    key, value = line.strip().split(" == ")
    result_m[key] = value


with open(file_name, mode="w", encoding="utf-8") as my_file:
    json.dump(result_m, my_file, ensure_ascii=False, indent=2)
# -

# N

# +
file_1 = input()
file_2 = input()

result_n: dict[str, dict[str, str]] = {}

with open(file_1, encoding="utf-8") as file:
    data = json.load(file)

with open(file_2, encoding="utf-8") as file:
    update = json.load(file)

for user in data:
    name = user.pop("name")

    result_n[name] = user


for user in update:
    name = user.pop("name")

    if name not in result_n:
        result_n[name] = {}

    for key in user:
        print(key)
        should_up = key not in result_n[name] or user[key] > result_n[name][key]

        if should_up:
            result_n[name][key] = user[key]

with open(file_1, mode="w", encoding="utf-8") as my_file:
    json.dump(result_n, my_file, ensure_ascii=False, indent=2)
# -

# O

# +
answers = (answer.strip() for answer in stdin.readlines())

file_name = "scoring.json"

points = 0

with open(file_name, encoding="UTF-8") as file:
    test_list = json.load(file)

for group in test_list:
    possible_points = group["points"]

    correct_amount = 0

    for test in group["tests"]:
        current_answer = next(answers)

        correct_answer = test["pattern"]

        if current_answer == correct_answer:
            correct_amount += 1

    group_points = (possible_points / len(group["tests"])) * correct_amount

    points += group_points

print(int(points))
# -

# P

# +
request = " ".join(input().lower().split())

result_p: list[str] = []

for file_p in stdin:
    with open(file_p.strip(), encoding="UTF-8") as my_file:
        if request in " ".join(my_file.read().lower().split()):
            result_p.append(file_p.strip())

print("\n".join(result_p) if result_p else "404. Not Found")
# -

# Q

# +
decoded_text = ""

with open("secret.txt", encoding="UTF-8") as file:
    coded_text = file.read()

    for char in coded_text:
        code = ord(char)
        code = code % 256 if code >= 128 else code
        decoded_text += chr(code)


print(decoded_text)
# -

# R

# +
file_name = input()

with open(file_name, encoding="UTF-8") as file:
    file.seek(0, 2)
    position = file.tell()

size: float = position

postfix = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
index = 0

while size > 1024 and index < len(postfix) - 1:
    index += 1
    size = size / 1024

print(f"{math.ceil(size)}{postfix[index]}")
# -

# S

# +
offset = int(input()) % 26

encoded = ""

a_code = ord("a")
z_code = ord("z")

with open("public.txt", encoding="UTF-8") as file:
    text = file.read()

    for char in text:
        lower = char.lower()

        is_upper = char.isupper()

        code = ord(lower)

        if code < a_code or code > z_code:
            encoded += char
            continue

        new_code = code + offset

        if new_code > z_code:
            new_code -= 26
        if new_code < a_code:
            new_code += 26

        encoded += chr(new_code).upper() if is_upper else chr(new_code)


with open("private.txt", mode="w", encoding="UTF-8") as file:
    file.write(encoded)
# -

# T
