# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

dir_name = os.getcwd()


def jump_in(dir_name):
    files_in_cd = os.listdir(dir_name)
    for i in files_in_cd:
        if os.path.isdir(i):
            continue
        else:
            print(i)
            cont = open(i, "r", encoding="utf-8")
            print(cont.read())


jump_in(dir_name)
