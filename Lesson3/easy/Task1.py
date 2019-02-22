
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    str_number = ''
    dot_index = str(number).find(".")
    for a in range(0, ndigits + dot_index + 1):
        str_number += str(number)[a]
    return str_number


print(my_round(2.1234567, 6))
print(my_round(2.1999967, 4))
print(my_round(2.9999967, 3))



