# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

current_dir = os.getcwd()


def add_dir(dir_name):

        os.mkdir(dir_name, 888)


def del_dir(dir_name):

        os.rmdir(dir_name)

# создаем директории


for i in range(1, 10):

    add_dir(f"{current_dir}/dir_{i}")


# удаляем директории

# for i in range(1, 10):
#
#     del_dir(f"{current_dir}/dir_{i}")
