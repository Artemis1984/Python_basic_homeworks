# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ["Банан", "Персик", "Яблоко", "Арбуз", "Виноград"]
fruits2 = ["Банан", "Киви", "Арбуз", "Вишня", "Груша"]

joined_fruits = [fruit for fruit in fruits1 if fruit == fruit in fruits2]

print(joined_fruits)
