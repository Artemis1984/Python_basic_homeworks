# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

import random

board = []

for a in range(8):
    temp = []
    for b in range(8):
        temp.append(" ")

    board.append(temp)


print("получаем произвольные, но уникальные координаты для размещения ферзей")

co_list = []
coordinates = []
x = 0
flag = True
while x < 8:
    for b in range(2):
        co_list.append(random.randint(0, 7))

    for c in coordinates:
        if c == co_list:
            flag = False
            break
    if flag:
        coordinates.append(co_list)
        co_list = []
        x += 1
    else:
        co_list = []
        continue

# заполняем координаты так, чтобы ферзи не били друг друга и проверим правильность работы программы
# по этой комбинации ферзи не бьют друг друга

# coordinates[0] = [1, 0]
# coordinates[1] = [4, 1]
# coordinates[2] = [6, 2]
# coordinates[3] = [0, 3]
# coordinates[4] = [2, 4]
# coordinates[5] = [7, 5]
# coordinates[6] = [5, 6]
# coordinates[7] = [3, 7]

print(coordinates)

for a in coordinates:
    board[a[0]][a[1]] = "*"


print("Рисуем доску с ферзями")
for a in board:
    print(a)


counter = 0


def checkmap(x, y):
    up(x, y)
    down(x, y)
    right(x, y)
    left(x, y)
    upleft(x, y)
    upright(x, y)
    downleft(x, y)
    downright(x, y)


def up(x, y):

    for i in range(y, y + 1):

        for j in range(x - 1, -1, -1):

            if board[j][i] == "*":
                global counter
                counter += 1


def down(x, y):

    for i in range(y, y + 1):

        for j in range(x + 1, len(board)):

            if board[j][i] == "*":
                global counter
                counter += 1


def right(x, y):

    for i in range(x, x + 1):

        for j in range(y + 1, len(board)):

            if board[i][j] == "*":
                global counter
                counter += 1


def left(x, y):

    for i in range(x, x + 1):

        for j in range(y - 1, -1, -1):

            if board[i][j] == "*":
                global counter
                counter += 1


def upleft(x, y):
    a = None
    if y - 1 > - 1:
        a = y - 1
    for i in range(x - 1, -1, -1):

        for j in range(1):
            if a is None:
                break

            if board[i][a] == "*":
                global counter
                counter += 1
            if a - 1 > -1:
                a -= 1
            else:
                a = None


def upright(x, y):
    a = None
    if y + 1 < len(board):
        a = y + 1
    for i in range(x - 1, -1, -1):

        for j in range(1):
            if a is None:
                break

            if board[i][a] == "*":
                global counter
                counter += 1
            if a + 1 < len(board):
                a += 1
            else:
                a = None


def downleft(x, y):
    a = None
    if y - 1 > - 1:
        a = y - 1
    for i in range(x + 1, len(board)):

        for j in range(1):
            if a is None:
                break

            if board[i][a] == "*":
                global counter
                counter += 1
            if a - 1 > - 1:
                a -= 1
            else:
                a = None


def downright(x, y):
    a = None
    if y + 1 < len(board):
        a = y + 1
    for i in range(x + 1, len(board)):

        for j in range(1):
            if a is None:
                break

            if board[i][a] == "*":
                global counter
                counter += 1
            if a + 1 < len(board):
                a += 1
            else:
                a = None


for i in coordinates:

    checkmap(i[0], i[1])

if counter > 0:
    print("ферзи бьют друг друга")
    counter = 0

else:
    print("ферзи не бьют друг друга")
    counter = 0
