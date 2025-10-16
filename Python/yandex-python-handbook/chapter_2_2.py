"""Задания к главе 2.2 "Условный оператор".

Хендбук Яндекс "Основы Python".
"""

# A

# +
from typing import TypedDict

name = input("Как Вас зовут?\n")
print(f"Здравствуйте, {name}!")
answer = input("Как дела?\n")

if answer == "хорошо":
    print("Я за Вас рада!")
else:
    print("Всё наладится!")
# -

# B

# +
petya = int(input())
vasya = int(input())

if petya > vasya:
    print("Петя")
else:
    print("Вася")
# -

# C

# +
petya = int(input())
vasya = int(input())
tolya = int(input())

if petya > vasya and petya > tolya:
    print("Петя")
elif vasya > tolya:
    print("Вася")
else:
    print("Толя")


# -

# D


# +
class Item(TypedDict):
    """Type array items."""

    name: str
    value: int


petya = int(input())
vasya = int(input())
tolya = int(input())

first_speed = max(petya, vasya, tolya)
third_speed = min(petya, vasya, tolya)

array: list[Item] = [
    {"name": "Петя", "value": petya},
    {"name": "Вася", "value": vasya},
    {"name": "Толя", "value": tolya},
]

array.sort(key=lambda obj: obj["value"], reverse=True)

for count, obj in enumerate(array):
    print(f"{count + 1}. {obj['name']}")
# -

# E

# +
added_petya = int(input())
added_vasya = int(input())

if added_petya + 6 > added_vasya + 12:
    print("Петя")
else:
    print("Вася")
# -

# F

# +
year = int(input())

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("YES")
else:
    print("NO")
# -

# G

# +
value = input()
reversed_value = value[::-1]

if reversed_value == value:
    print("YES")
else:
    print("NO")
# -

# H

# +
string = input()

if "зайка" in string:
    print("YES")
else:
    print("NO")
# -

# I

# +
first_value, second_value, third_value = input(), input(), input()

my_array = [first_value, second_value, third_value]
my_array.sort()

print(my_array[0])
# -

# J

# +
value = input()

sum1 = int(value[1]) + int(value[2])
sum2 = int(value[0]) + int(value[1])

if sum1 >= sum2:
    print(str(sum1) + str(sum2))
else:
    print(str(sum2) + str(sum1))
# -

# K

# +
value = input()

digits = list(map(int, value))
digits.sort()

if digits[0] + digits[2] == digits[1] * 2:
    print("YES")
else:
    print("NO")
# -

# L

# +
line1 = int(input())
line2 = int(input())
line3 = int(input())

if all([line1 + line2 > line3, line1 + line3 > line2, line2 + line3 > line1]):
    print("YES")
else:
    print("NO")
# -

# M

# +
line_1 = input()
line_2 = input()
line_3 = input()

for index, _ in enumerate(line_1):
    if line_1[index] == line_2[index] == line_3[index]:
        print(line_1[index])
# -

# N

# +
integers_list = list(map(int, input()))
integers_list.sort()

first = "0"
second = "0"

if integers_list[0] != 0:
    first = str(integers_list[0]) + str(integers_list[1])
elif integers_list[1] != 0:
    first = str(integers_list[1]) + str(integers_list[0])
elif integers_list[2] != 0:
    first = str(integers_list[2]) + str(integers_list[0])

if integers_list[2] != 0:
    second = str(integers_list[2]) + str(integers_list[1])

print(first, second)
# -

# O

# +
value1 = list(map(int, input()))
value2 = list(map(int, input()))
combined = value1 + value2

combined.sort(reverse=True)


result = f"{combined[0]}{(combined[1] + combined[2]) % 10}{combined[3]}"

print(result)
# -

# P

# +
vasya_p = "Вася"
tolya_p = "Толя"
petya_p = "Петя"


p_s = int(input())
v_s = int(input())
t_s = int(input())

if v_s > t_s > p_s:
    first = vasya_p
    second = tolya_p
    third = petya_p
elif v_s > p_s > t_s:
    first = vasya_p
    second = petya_p
    third = tolya_p
elif p_s > v_s > t_s:
    first = petya_p
    second = vasya_p
    third = tolya_p
elif p_s > t_s > v_s:
    first = petya_p
    second = tolya_p
    third = vasya_p
elif t_s > p_s > v_s:
    first = tolya_p
    second = petya_p
    third = vasya_p
else:
    first = tolya_p
    second = vasya_p
    third = petya_p


print(f'{"": ^8}{first: ^8}{"": ^8}')
print(f'{second: ^8}{"": ^8}{"": ^8}')
print(f'{"": ^8}{"": ^8}{third: ^8}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')
# -

# Q

# +
a_coef = float(input())
b_coef = float(input())
c_coef = float(input())


if a_coef == b_coef == c_coef == 0:
    print("Infinite solutions")
elif a_coef == b_coef == 0:
    print("No solution")
elif a_coef == 0:
    result_q = -c_coef / b_coef

    print(round(result_q, 2))
else:
    discriminant = b_coef**2 - 4 * a_coef * c_coef

    if discriminant < 0:
        print("No solution")
    elif discriminant == 0:
        result_q = -b_coef / (2 * a_coef)

        print(round(result_q, 2))
    else:
        result1 = (-b_coef + discriminant**0.5) / (2 * a_coef)
        result2 = (-b_coef - discriminant**0.5) / (2 * a_coef)

        min_result = min(round(result1, 2), round(result2, 2))
        max_result = max(round(result1, 2), round(result2, 2))

        print(min_result, max_result)
# -

# R

# +
a_length = float(input())
b_length = float(input())
c_length = float(input())

lengths = [a_length, b_length, c_length]
lengths.sort(reverse=True)

longest = lengths[0]
other1, other2 = lengths[1:]

if longest**2 == other1**2 + other2**2:
    print("100%")
elif longest**2 > other1**2 + other2**2:
    print("велика")
else:
    print("крайне мала")
# -

# T

# +
a_str = input()
b_str = input()
c_str = input()

results = []

for string in [a_str, b_str, c_str]:
    if "зайка" in string:
        results.append(string)

results.sort()
result = results[0]

print(result, len(result))
