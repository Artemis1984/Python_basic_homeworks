# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2
print("первое число:", number1, "второе число:", number2)


