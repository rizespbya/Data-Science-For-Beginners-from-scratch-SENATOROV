# %%
"""Задания к главе 6.3.

Модуль requests

Хендбук Яндекс "Основы Python".
"""

# A

# %%
import sys

from requests import delete, get, post, put

base_host = "http://127.0.0.1:5000"

response = get(base_host, timeout=5000)

message = response.content.decode("utf-8")

print(message)

# B

# %%
base_host = f"http://{input()}"

result = 0

while response_b := int(get(base_host, timeout=5000).text):
    result += response_b

print(result)

# C

# %%
base_host = f"http://{input()}"

response_c = get(base_host, timeout=5000).json()

sum_c = 0
for item in response_c:
    sum_c += item if isinstance(item, int) else 0

print(sum_c)

# D

# %%
base_host = f"http://{input()}"
key = input()

response_d = get(base_host, timeout=5000).json()

print(response_d.get(key, "No data"))

# E

# %%
host, *paths = map(str.strip, sys.stdin)

results = [get(f"http://{host}{path}", timeout=5000).json() for path in paths]

print(sum(sum(nums) for nums in results))

# F

# %%
host = f"http://{input()}"

users = get(f"{host}/users", timeout=5000).json()

names = list(
    map(lambda user: f"{user['last_name']} {user['first_name']}", users)
)

print("\n".join(sorted(names)))

# G

# %%
host = f"http://{input()}"
user_id = input()

text = "".join(string for string in sys.stdin)


try:
    user = get(f"{host}/users/{user_id}", timeout=5000).json()
except ValueError:
    print("Пользователь не найден")
else:
    for key in user:
        text = text.replace(f"{{{key}}}", str(user[key]))
    print(text)

# H

# %%
keys = ["username", "last_name", "first_name", "email"]

host, *data = map(str.strip, sys.stdin)

user_dict: dict[str, str] = dict(zip(keys, data))

post(f"http://{host}/users/", json=user_dict, timeout=5000)

# I

# %%
host, user_id, *updated_data = map(str.strip, sys.stdin)

updated_data_dict: dict[str, str] = dict(
    map(lambda item: item.split("="), updated_data)
)

print(updated_data_dict)
put(f"http://{host}/users/{user_id}", json=updated_data_dict, timeout=5000)

# J

# %%
host, user_id = map(str.strip, sys.stdin)

delete(f"http://{host}/users/{user_id}", timeout=5000)
