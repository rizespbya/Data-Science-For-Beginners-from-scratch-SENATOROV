"""Задания к главе 2.4 "Вложенные циклы" из хендбука Яндекс "Основы Python"."""

# A

# +
num_a = int(input())

for index1 in range(1, num_a + 1):
    for index2 in range(1, num_a + 1):
        print(index1 * index2, end="\n" if index2 == num_a else " ")
# -

# B

# +
num_b = int(input())

for index1 in range(1, num_b + 1):
    for index2 in range(1, num_b + 1):
        print(f"{index2} * {index1} = {index2 * index1}")
# -

# C

# +
max_num = int(input())

current = 1

current_row = 1
current_column = 1

while current <= max_num:
    while current <= max_num and current_column <= current_row:
        print(current, end=" ")

        current += 1
        current_column += 1

    current_column = 1
    current_row += 1
    print()
# -

# D

# +
inputs_amount = int(input())

inputs_list = [input() for _ in range(inputs_amount)]

sums_list = map(lambda item: sum(map(int, item)), inputs_list)

print(sum(sums_list))
# -

# E

# +
lands_amount = int(input())

bunnies_counter = 0

for _ in range(lands_amount):
    is_bunny_found = False

    while (description := input()) != "ВСЁ":
        if description == "зайка" and not is_bunny_found:
            bunnies_counter += 1
            is_bunny_found = True

print(bunnies_counter)
# -

# F

# +
nums_amount = int(input())

nums_list = [int(input()) for _ in range(nums_amount)]

divider = nums_list[0]

for index in range(1, len(nums_list), 1):
    next_var = nums_list[index]

    while next_var:
        divider, next_var = next_var, divider % next_var

print(divider)
# -

# G

# +
players_amount = int(input())

seconds = 3

for index in range(players_amount):
    current_time = seconds

    while current_time:
        print(f"До старта {current_time} секунд(ы)")
        current_time -= 1

    print(f"Старт {index + 1}!!!")

    seconds += 1
# -

# H

# +
children_amount = int(input())

winner_name: str
max_sum: int = 0

for _ in range(children_amount):
    name = input()
    guessed_num = input()

    current_sum = sum(map(int, guessed_num))

    if current_sum >= max_sum:
        max_sum = current_sum
        winner_name = name

print(winner_name)
# -

# I

# +
children_amount = int(input())

largest_num = ""

for _ in range(children_amount):
    largest_num += max(input())

print(largest_num)
# -

# J

# +
slices = int(input())

print("А Б В")
for index1 in range(1, slices + 1):
    for index2 in range(1, slices + 1):
        for index3 in range(1, slices + 1):
            total_sum = index1 + index2 + index3
            if total_sum == slices:
                print(f"{index1} {index2} {index3}")
                break

            if total_sum > slices:
                break
# -

# K

# +
nums_amount = int(input())

primes = 0

for _ in range(nums_amount):
    is_prime = True

    num = int(input())

    if num < 2:
        continue

    for divider in range(2, round(num / 2) + 1):
        if num % divider == 0:
            is_prime = False
            break

    if is_prime:
        primes += 1

print(primes)
# -

# L

# +
height = int(input())
width = int(input())

cell_value = 1

chars_amount = len(str(height * width))

for row_index in range(height):
    for column_index in range(width):
        end = " " if column_index < width - 1 else "\n"
        display_value = str(cell_value).rjust(chars_amount)

        print(display_value, end=end)

        cell_value += 1
# -

# M

# +
height_m = int(input())
width_m = int(input())


chars_amount_m = len(str(height_m * width_m))

first_num_in_row = 1

for row_index in range(height_m):
    for column_index in range(width_m):
        end = " " if column_index < width_m - 1 else "\n"

        value = first_num_in_row + height_m * column_index

        print(str(value).rjust(chars_amount_m), end=end)

    first_num_in_row += 1
# -

# N

# +
height_n = int(input())
width_n = int(input())


length = len(str(height_n * width_n))

is_odd = True

for row_index in range(1, height_n + 1):

    current_range = range(1, width_n + 1) if is_odd else range(width_n, 0, -1)

    for column_index in current_range:
        value = (row_index - 1) * width_n + column_index

        print(str(value).rjust(length), end=" ")

    print()

    is_odd = not is_odd
# -

# O

# +
height_o = int(input())
width_o = int(input())


length_o = len(str(height_o * width_o))


for row_index in range(0, height_o):

    for column_index in range(0, width_o):

        if column_index % 2 != 0:
            value = (column_index + 1) * height_o - row_index
        else:
            value = column_index * height_o + row_index + 1

        print(str(value).rjust(length_o), end=" ")

    print()
# -

# P

# +
size = int(input())
width_p = int(input())


for row_index in range(1, size + 1):
    temp: list[str] = []

    for column_index in range(1, size + 1):
        product = str(row_index * column_index)

        additional_space = " " if width_p % 2 else ""

        string = (product + additional_space).center(width_p)

        temp.append(string)

    print("|".join(temp))

    if row_index < size:
        print(f"{'-' * (size * (width_p + 1) - 1)}")
# -

# Q

# +
nums_amount = int(input())

counter = 0

for _ in range(nums_amount):
    current_value = input()

    if current_value == current_value[::-1]:
        counter += 1

print(counter)
# -

# R

# +
limit = int(input())

counter = 1

level = 1

result: list[list[str]] = []

while counter <= limit:
    current_list: list[str] = []

    for _ in range(level):
        current_list.append(str(counter))
        counter += 1

        if counter > limit:
            break

    result.append(current_list)
    level += 1

formatted_result = list(map(" ".join, result))
max_length = len(formatted_result[-1])

for string in formatted_result:
    print(f"{string:^{max_length}}")
# -

# S

# +
square_size = int(input())

cell_width = len(str(round(square_size / 2)))

for row_index in range(1, square_size + 1):
    for column_index in range(1, square_size + 1):
        value = min(
            row_index,
            column_index,
            square_size + 1 - row_index,
            square_size + 1 - column_index,
        )

        formatted_value = str(value).rjust(cell_width)

        print(formatted_value, end=" ")
    print()
# -

# T

# +
value_t = int(input())


def convert_to_base(number: int, base: int) -> str:
    """Преобразует натуральное число в заданную систему счисления.

    Args:
        number (int): натуральное число
        base (int): основание системы счисления от 2 до 10

    Returns:
        int: Строковое представление числа number в системе счисления base
    """
    digits = "0123456789"
    result_str = ""

    while number > 0:
        result_str = digits[number % base] + result_str
        number //= base

    return result_str


max_sum = 0
max_base: int

for current_base in range(2, 11):
    converted_value = str(convert_to_base(value_t, current_base))

    current_sum = sum(map(int, converted_value))

    if current_sum > max_sum:
        max_sum = current_sum
        max_base = current_base

print(max_base)
