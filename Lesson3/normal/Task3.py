# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# print(list(filter(lambda x: x >= 4, [1, 2, 3, 4, 5, 6, 7])))

my_list = [1, 2, 3, 4, 5, 6, 7]

print("До", my_list)


def filtering(a, condition):
    index = 0
    while index < len(a):
        if a[index] <= condition:
            a.pop(index)
        else:
            index += 1


filtering(my_list, 4)
print("После", my_list)
