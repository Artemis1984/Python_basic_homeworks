# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3


i = 1
temp_list = []
apartments = []
block = 6
spaces = 1
for a in range(block + 1):
    for b in range(a):
        for c in range(a):
            temp_list.append(i)
            i += 1
        apartments.append(temp_list)
        temp_list = []

for a in range(len(apartments)-1, -1, -1):
    try:
        if len(apartments[a]) < len(apartments[a + 1]):
            spaces += 2
    except IndexError:
        pass
    print(end=" " * spaces)
    for b in range(len(apartments[a])):

        print("{:^2}".format(apartments[a][b]), end="  ")
    print()

search = int(input("Введите число для поиска комнаты: "))

for i in range(len(apartments)):
    for j in range(len(apartments[i])):
        if apartments[i][j] == search:
            print(i+1, j+1)

