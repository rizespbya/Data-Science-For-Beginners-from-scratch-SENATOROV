"""Задания к главе 2.3 "Циклы" из хендбука Яндекс "Основы Python"."""

# A

# +
while value := input() != "Три!":
    print("Режим ожидания...")

print("Ёлочка, гори!")
# -

# B

# +
counter = 0

while (value_b := input()) != "Приехали!":
    if "зайка" in value_b:
        counter += 1

print(counter)
# -

# C

# +
start = int(input())
finish = int(input())

result = []

for index in range(start, finish + 1):
    result.append(index)


print(" ".join(map(str, result)))
# -

# D

# +
start = int(input())
finish = int(input())

one = 1 if finish > start else -1

for i in range(start, finish + one, one):
    print(i, end=" ")
# -

# E

# +
total = 0.0

while (price := float(input())) != 0:
    total += price * 0.9 if price >= 500 else price

print(total)
# -

# F

# +
a_variable = int(input())
b_variable = int(input())

while b_variable:
    a_variable, b_variable = b_variable, a_variable % b_variable

print(a_variable)
# -

# G

# +
a_coef = int(input())
b_coef = int(input())

x_coef = a_coef
y_coef = b_coef

while y_coef:
    x_coef, y_coef = y_coef, x_coef % y_coef

print(int(a_coef * b_coef / x_coef))
# -

# H

# +
text_h = input()
num_h = int(input())

for i in range(0, num_h, 1):
    print(text_h)
# -

# I

# +
input_x = int(input())

result_i = 1

for i in range(1, input_x + 1):
    result_i *= i

print(result_i)
# -

# J

# +
x_coord = y_coord = 0

while (direction := input()) != "СТОП":
    num = int(input())

    match direction:
        case "СЕВЕР":
            y_coord += num
        case "ЮГ":
            y_coord -= num
        case "ВОСТОК":
            x_coord += num
        case "ЗАПАД":
            x_coord -= num

print(y_coord)
print(x_coord)
# -

# K

# +
string = input()

i = 0

total_sum = 0

while i < len(string):
    total_sum += int(string[i])
    i += 1

print(total_sum)
# -

# L

# +
string = input()

res = 0

for digit in string:
    res = max(res, int(digit)) if res is not None else int(digit)

print(res)
# -

# M

# +
num = int(input())

names = [input() for _ in range(0, num)]

result_m = names[0]

for name in names[1::]:
    result_m = name if name < result_m else result_m

print(result_m)
# -

# N

# +
num = int(input())

if num < 2:
    print("NO")
else:
    for i in range(2, round(num / 2) + 1):
        if num % i == 0:
            print("NO")
            break
    else:
        print("YES")
# -

# O

# +
num = int(input())

my_list = [input() for _ in range(num)]

print(len(list(filter(lambda string: "зайка" in string, my_list))))
# -

# P

# +
num_p = input()

left_p = 0
right_p = len(num_p) - 1

while left_p < right_p:
    if num_p[left_p] != num_p[right_p]:
        print("NO")

        break
    left_p += 1
    right_p -= 1
else:
    print("YES")
# -

# Q

# +
num_q = input()

print("".join(filter(lambda digit: int(digit) % 2 != 0, num_q)))
# -

# R

# +
num = int(input())

rest = num

result_int: list[int] = []

divider = 1

while rest > 1:
    divider += 1

    if rest % divider != 0:
        continue

    result_int.append(divider)

    rest //= divider

    divider -= 1

result_str = " * ".join(map(str, result_int))

print(result_str if num > 1 else num)
# -

# S

# +
left = 1
right = 1001

print((left + right) // 2)

while (response := input()) != "Угадал!":
    if response == "Больше":
        left = (left + right) // 2 + 1
    else:
        right = (left + right) // 2 - 1

    print((left + right) // 2)
# -

# T
