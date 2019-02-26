# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

origin_list = [i for i in range(random.randint(-5, 5), 5)]
print(origin_list)
new_list = list(map(lambda x: x**2, origin_list))
both_list = list(zip(origin_list, new_list))
print(both_list)
