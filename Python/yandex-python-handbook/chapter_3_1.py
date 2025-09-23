"""Задания к главе 3.1 "Строки, кортежи, списки".

Хендбук Яндекс "Основы Python".
"""

# A

# +
import math

words_amount = int(input())

for _ in range(words_amount):
    word = input()
    if word[0] not in "абв":
        print("NO")
        break
else:
    print("YES")
# -

# B

# +
hor_str = input()

for char in hor_str:
    print(char)
# -

# C

# +
max_length = int(input())
titles_amount = int(input())

for _ in range(titles_amount):
    title = input()

    if len(title) > max_length:
        end = max_length - 3
        title = title[0:end:] + "..."

    print(title)
# -

# D

while (input_str := input()) != "":
    if input_str.endswith("@@@"):
        continue

    if input_str.startswith("##"):
        print(input_str[2::])
    else:
        print(input_str)

# E

# +
input_str = input().lower()

if input_str == input_str[::-1]:
    print("YES")
else:
    print("NO")
# -

# F

# +
lands_amount = int(input())

rabbits_counter = 0
for _ in range(lands_amount):
    rabbits_counter += (land := input()).count("зайка")

print(rabbits_counter)
# -

# G

# +
two_numbers = input()

print(sum(map(int, two_numbers.split())))
# -

# H

# +
lands_amount = int(input())

for _ in range(lands_amount):
    land = input()

    position = land.find("зайка")

    print(position + 1 if position >= 0 else "Заек нет =(")
# -

# I

while line := input():
    hash_position = line.find("#")

    match (hash_position):
        case -1:
            print(line)
        case 0:
            continue
        case _:
            print(line[0:hash_position:])

# J

# +
letters: list[str] = []

while (line := input()) != "ФИНИШ":
    letters.extend(list("".join(line.lower().split(" "))))

letters.sort()

max_count = 0
max_count_char: str

for char in letters:
    current_count = letters.count(char)

    if current_count > max_count:
        max_count = current_count
        max_count_char = char

print(max_count_char)
# -

# K

# +
titles_amount = int(input())

titles = [input() for _ in range(titles_amount)]

search_request = input().lower()

for title in titles:
    if title.lower().find(search_request) != -1:
        print(title)
# -

# L

# +
porridge_list = [
    "Манная",
    "Гречневая",
    "Пшённая",
    "Овсяная",
    "Рисовая",
]


days_amount = int(input())

for day in range(days_amount):
    print(porridge_list[day % len(porridge_list)])
# -

# M

# +
nums_amount = int(input())

nums: list[int] = [int(input()) for _ in range(nums_amount)]

power = int(input())

for num in nums:
    print(num**power)
# -

# N

# +
nums_iter = map(int, input().split(" "))

power = int(input())

for num in nums_iter:
    print(num**power, end=" ")
# -

# O

# +
nums_list = list(map(int, input().split(" ")))

divider = nums_list[0]

for index in range(1, len(nums_list), 1):
    next_var = nums_list[index]

    while next_var:
        divider, next_var = next_var, divider % next_var

print(divider)
# -

# P


# Q

# +
input_string = "".join(input().lower().split(" "))

print("YES" if input_string == input_string[::-1] else "NO")
# -

# R

# +
input_string = input()

length = len(input_string)

counter = 0

for index, digit in enumerate(input_string):
    counter += 1

    if index < length - 1 and input_string[index + 1] == digit:
        continue

    print(digit, counter)
    counter = 0
# -

# S

# +
input_list = input().split(" ")

stack_s: list[int] = []


for item in input_list:
    if item.isdigit():
        stack_s.append(int(item))
        continue

    second = stack_s.pop()
    first = stack_s.pop()

    match (item):
        case "+":
            stack_s.append(first + second)
        case "-":
            stack_s.append(first - second)
        case "*":
            stack_s.append(first * second)

print(stack_s[0])
# -

# T

# +
input_list = input().split(" ")

stack: list[int] = []


for item in input_list:
    if item.isdigit():
        stack.append(int(item))
        continue

    match (item):
        case "+":
            second = stack.pop()
            first = stack.pop()
            stack.append(first + second)

        case "-":
            second = stack.pop()
            first = stack.pop()
            stack.append(first - second)

        case "*":
            second = stack.pop()
            first = stack.pop()
            stack.append(first * second)

        case "/":
            second = stack.pop()
            first = stack.pop()
            stack.append(first // second)

        case "~":
            first = stack.pop()
            stack.append(first * (-1))

        case "!":
            first = stack.pop()
            stack.append(math.factorial(first))

        case "#":
            stack.append(stack[-1])

        case "@":
            stack.append(stack.pop(-3))

print(stack[0])
