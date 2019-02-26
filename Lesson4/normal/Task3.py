# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import os
import random
import re

path = os.path.join("/Users/paruyr1/Desktop", 'text.txt')
with open(path, 'w') as f:

    for a in range(2500):
        f.write(str(random.randint(1, 9)))
with open(path, 'r') as f:
    print("содержимое файла:", f.readlines())

with open(path, 'r', encoding='utf-8') as f:

    for a in f:
        long_number = re.findall(r"1+(?=1)|2+(?=2)|3+(?=3)|4+(?=4)|5+(?=5)|6+(?=6)|7+(?=7)"
                                 r"|8+(?=8)|9+(?=9)", a)

lS = []
maximum = 0
for b in long_number:
    if maximum < len(b):
        maximum = len(b)
        lS.clear()
        lS.append(b)

print("самая длинная ппоследовательность цифр равна :", maximum, lS)
