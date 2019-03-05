# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class School:

    def __init__(self, classrooms):

        self.classrooms = classrooms

    def get_classes(self):

        print("Все классы школы", end=" ")
        for grade in self.classrooms:
            print(grade.class_name, end=" ")
        print()

    def find_pupil(self, pupil):
        for grade in self.classrooms:
            if pupil in grade.pupils:
                print("Ученик", pupil.name, "класса", grade.class_name, end=" ")
                for teacher in grade.teachers:
                    print("Учитель", teacher.name, "предмет", teacher.subject, end=" ")


class Grade:

    def __init__(self, class_name, pupils, teachers):

        self.class_name = class_name
        self.pupils = pupils
        self.teachers = teachers

    def get_pupils(self):

        print("Ученики класса", self.class_name, end=" ")
        for pupil in self.pupils:
            print(pupil.name, end=", ")
        print()

    def get_teachers(self):

        print("Учителя класса", self.class_name, end=" ")
        for teacher in self.teachers:
            print(teacher.name, teacher.subject, end=", ")
        print()


class Teacher:

    def __init__(self, name, subject):

        self.name = name
        self.subject = subject

    def get_teacher(self):

        print("Учитель", self.name, "преподает", self.subject)


class Pupil:

    def __init__(self, mother_name, father_name, name):

        self.mother_name = mother_name
        self.father_name = father_name
        self.name = name

    def get_parent_name(self):

        print("Родители ученика", self.name, "Мама", self.mother_name, "Папа", self.father_name)

    def get_info(self):
        print(self.name, )


pupil1 = Pupil("Иванова С.И", "Сергеев В.Н", "Сергеев Н.В")
pupil2 = Pupil("Петрова С.И", "Сидоров В.Н", "Сидоров Н.В")
pupils1 = [pupil1, pupil2]

pupil3 = Pupil("Шишкова С.И", "Калимов В.Н", "Калимов Н.В")
pupil4 = Pupil("Касьянова С.И", "Леонов В.Н", "Леонов Н.В")
pupils2 = [pupil3, pupil4]


teacher1 = Teacher("Тарасов В.Б", "Математика")
teacher2 = Teacher("Ермолов А.Н", "История")
teachers1 = [teacher1, teacher2]

grade7 = Grade("7А", pupils1, teachers1)
grade8 = Grade("8Б", pupils2, teachers1)

grades = [grade7, grade8]

school = School(grades)

# список всех классов школы
school.get_classes()

# список всех учеников в классе
grade7.get_pupils()
grade8.get_pupils()

# список всех учителей в классе
grade7.get_teachers()
grade8.get_teachers()

# ФИО родителей указанного ученика
pupil1.get_parent_name()

# (Ученик --> Класс --> Учителя --> Предметы)
print("*" * 50)
school.find_pupil(pupil1)
