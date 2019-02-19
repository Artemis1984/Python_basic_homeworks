# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

first_list = ["арбуз", "виноград", "банан", "яблоко"]
second_list = ["арбуз", "авокадо", "банан", "персик"]
i = 0
while i < len(first_list):
    for a in second_list:
        if first_list[i] == a:
            first_list.remove(first_list[i])
        else:
            i += 1

print(first_list)
