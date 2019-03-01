# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def ls():
    print(os.path.abspath((os.getcwd())))


def cd(path):
    os.chdir(os.path.abspath(path))


def rm(file_name):
    confirm = input("Введите да, чтобы подтвердить операцию")
    if confirm == "да":
        os.remove(file_name)


def cp(file_name):
    shutil.copy(file_name, file_name + "copy")


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


argument = None

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

while True:

    operation = input("Выберите операцию: ")
    if operation == "cp" or operation == "rm" or operation == "cd":
        argument = input("Введите параметр для метода")

    if operation == "cp":
        try:
            cp(argument)
        except OSError:
            print("что-то пошло не так")
    elif operation == "rm":
        try:
            rm(argument)
        except OSError:
            print("что-то пошло не так")
    elif operation == "cd":
        try:
            cd(argument)
        except OSError:
            print("что-то пошло не так")
    elif operation == "ls":
        try:
            ls()
        except OSError:
            print("что-то пошло не так")
