# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for a in range(len(origin_list)):
        for b in range(len(origin_list)):
            if origin_list[a] < origin_list[b]:
                buff = origin_list[b]
                origin_list[b] = origin_list[a]
                origin_list[a] = buff
    print(origin_list)


sort_to_max([120, 230, 2, 10, -12, 2.5, 20, -11, 4, 4, 0])


