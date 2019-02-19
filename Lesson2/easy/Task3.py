# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

first_list = []

for a in range(1, 11):
    first_list.append(a)

print(first_list)

new_list = []

for b in first_list:
    if b % 2 == 0:
        b /= 4
        new_list.append(b)
    else:
        b *= 2
        new_list.append(b)

print(new_list)
