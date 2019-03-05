# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


import math


class Triangle:

    def __init__(self, a1, a2, b1, b2, c1, c2):

        self.a = math.sqrt((c2 - a2) ** 2 + (c1 - a1) ** 2)
        self.b = math.sqrt((b2 - a2) ** 2 + (b1 - a1) ** 2)
        self.c = math.sqrt((c2 - b2) ** 2 + (c1 - b1) ** 2)

    def get_height(self):

        try:
            p = 0.5 * (self.a + self.b + self.c)
            height = (2 * math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))) / self.a
            return height
        except ValueError:
            print("Координаты введены неверно")

    def square(self):
        if self.get_height():
            s = 0.5 * self.a * self.get_height()
            print("Площадь треугольника", s)

    def perimeter(self):
        per = self.a + self.b + self.c
        print("Периметр треугольника", per)


triangle1 = Triangle(0, 0, 10, 6, 0, 20)
print("Высота треугольника", triangle1.get_height())
triangle1.square()
triangle1.perimeter()
print()
triangle2 = Triangle(0, 0, 5, 5, 0, 10)
print("Высота треугольника", triangle2.get_height())
triangle2.square()
triangle2.perimeter()
