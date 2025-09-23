"""Задания к главе 2.1 Ввод и вывод данных.

Операции с числами, строками. Форматирование. из хендбука Яндекс Основы Python.
"""

# A

print("Привет, Яндекс!")

# B

name = input("Как Вас зовут?")
print(f"Привет, {name}")

# C

string = input()
for _ in range(3):
    print(string)

# D

# +
money = int(input())

price = 38 * 5 // 2

rest = money - price

print(rest)
# -

# E

# +
price = int(input())
weight = int(input())
money = int(input())

print(money - price * weight)
# -

# F

# +
title = input()
price = int(input())
weight = int(input())
money = int(input())

total_price = price * weight
rest = money - total_price

print("Чек")
print(f"{title} - {weight}кг - {price}руб/кг")
print(f"Итого: {total_price}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {rest}руб")
# -

# G

# +
num = int(input())

for _ in range(num):
    print("Купи слона!")
# -

# H

# +
num = int(input())

title = input()

for _ in range(num):
    print(f'Я больше никогда не буду писать "{title}"!')
# -

# I

# +
children = int(input())
minutes = int(input())

child_eat_per_minute = 2 / 2 / 2

result = int(children * minutes * child_eat_per_minute)
print(result)
# -

# J

# +
name = input()
locker_number = int(input())

group_number = locker_number // 100
child_number = locker_number % 10
bed_number = (locker_number // 10) % 10


print("Группа №{group_number}.")
print("{child_number}. {name}.")
print("Шкафчик: {locker_number}.")
print("Кроватка: {bed_number}.")
# -

# K

# +
number = int(input())

first = number // 1000
second = (number // 100) % 10
third = (number // 10) % 10
fourth = number % 10

result = second * 1000 + first * 100 + fourth * 10 + third

print(result)
# -

# L

# +
first_value = input().zfill(3)
second_value = input().zfill(3)

result_str: str = ""

for index in range(2, -1, -1):
    current_sum = (int(first_value[index]) + int(second_value[index])) % 10
    result_str = f"{current_sum}{result}"

print(result_str.lstrip("0"))
# -

# M

# +
children = int(input())
candies = int(input())

for_each = candies // children
rest = candies % children

print(for_each)
print(rest)
# -

# N

# +
red = int(input())
green = int(input())
blue = int(input())

print(red + blue + 1)
# -

# O

# +
hours = int(input())
minutes = int(input())
time = int(input())

time_hours = time // 60
time_minutes = time % 60

result_minutes = (minutes + time_minutes) % 60
result_hours = (hours + time_hours + (minutes + time_minutes) // 60) % 24

print(f"{str(result_hours).zfill(2)}:{str(result_minutes).zfill(2)}")
# -

# P

# +
start = int(input())
finish = int(input())
speed = int(input())

result_time: float = (finish - start) / speed

print(f"{result_time:.2f}")
# -

# Q

# +
rest = int(input())
last = int(input(), 2)

print(rest + last)
# -

# R

# +
price = int(input(), 2)
money = int(input())

print(money - price)
# -

# S

# +
title = input()
price = int(input())
weight = int(input())
money = int(input())

total_price = weight * price
change = money - total_price

weight_with_price_display = f"{weight}кг * {price}руб/кг"
total_price_display = f"{total_price}руб"
money_display = f"{money}руб"
change_display = f"{change}руб"

LENGTH = 35

line1 = "Чек".center(LENGTH, "=")
line2 = f"{'Товар:': <10}{title: >25}"
line3 = f"{'Цена:': <10}{weight_with_price_display: >25}"
line4 = f"{'Итого:': <10}{total_price_display: >25}"
line5 = f"{'Внесено:': <10}{money_display: >25}"
line6 = f"{'Сдача:': <10}{change_display: >25}"
line7 = "=" * LENGTH

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)
# -

# T

# +
weight = int(input())
price = int(input())
price1 = int(input())
price2 = int(input())

# Составим систему уравнений с двумя неизвестными weight1 и weight2
# weight1 * price1 + weight2 * price2 = weight * price
# weight1 + weight2 = weight
#
# weight1 = weight - weight2
#
# (weight - weight2) * price1 + weight2 * price2 = weight * price
# weight * price1 - weight2 * price1 + weight2 * price2  = weight * price
# weight2 * (price2 - price1) = weight * price - weight * price1
# weight2 = (weight * price - weight * price1) / (price2 - price1)

weight2 = (weight * price - weight * price1) / (price2 - price1)

weight1 = weight - weight2


print(int(weight1), int(weight2))
