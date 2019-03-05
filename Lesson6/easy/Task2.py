# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math


class Trapeze:

    def __init__(self, a1, a2, b1, b2, c1, c2, d1, d2):

        self.a = math.sqrt((d2 - a2)**2 + (d1 - a1)**2)
        self.b = math.sqrt((b2 - a2)**2 + (b1 - a1)**2)
        self.c = math.sqrt((c2 - b2)**2 + (c1 - b1)**2)
        self.d = math.sqrt((c2 - d2)**2 + (c1 - d1)**2)
        self.parallel_bases = d1 - a1 == c1 - b1

    def check_trapeze(self):
        if self.b == self.d and self.c != 0 and self.parallel_bases:
            print("фигура является равнобочной трапецией")
            return True
        else:
            print("фигура не является равнобочной трапецией")
            return False

    def perimeter(self):
        p = self.a + self.b + self.c + self.d
        print("периметр трапеции", p)

    def get_height(self):
        height = math.sqrt(self.b**2 - (((self.a - self.c)**2 + self.b**2 - self.d**2) / 2 * (self.a - self.c))**2)
        return height

    def square(self):
        s = 0.5 * (self.a + self.b) * self.get_height()
        print("площадь трапеции", s)

    def side_length(self):
        print("длины сторон ", self.b + self.d)

    def info(self):
        if self.check_trapeze():
            self.side_length()
            self.perimeter()
            self.square()


trapeze1 = Trapeze(0, 0, 5, 1, 5, 5, 0, 6)
trapeze1.info()
print()
trapeze2 = Trapeze(0, 0, 5, 1, 6, 7, 2, 5)
trapeze2.info()
