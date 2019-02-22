# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    fib_list = [1, 1]
    for a in range(m + 1):
        fib_list.append(fib_list[a] + fib_list[a+1])
    return fib_list[n:m]


print(fibonacci(5, 12))

