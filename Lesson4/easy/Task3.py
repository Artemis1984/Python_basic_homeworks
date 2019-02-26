# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

origin_list = [random.randint(-10, 13) for _ in range(15)]
print("произвольный спсиок", origin_list)
new_list = [item for item in origin_list if item % 3 == 0 and item > 0 and item % 4 != 0]
print("отфильтрованный спсиок", new_list)
