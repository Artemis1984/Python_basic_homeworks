# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


class Employee:

    def __init__(self):

        self.employees = []
        self.work_hours = []

    def payroll(self):

        workers = open("workers", "r", encoding="utf-8")
        hours = open("hourse_of", "r", encoding="utf-8")

        for line in workers:
            self.employees.append(line)

        self.employees[0] = self.employees[0].rstrip("\n") + "{:>16} {:>11}".format("Отработано", "Итого")

        for line in hours:
            self.work_hours.append(line)

        for i in range(0, len(self.employees)):

            if i == 0:
                print(self.employees[i].rstrip("\n"))
                continue

            for j in range(1, len(self.work_hours)):

                if self.employees[i][:21] == self.work_hours[j][:21]:
                    result = int(self.work_hours[j][-4:]) - int(self.employees[i][-4:])

                    if result < 0:
                        proportion = abs(result) / (int(self.employees[i][-4:]) / 100)
                        salary = int(self.employees[i][20:26]) - (int(self.employees[i][20:26]) * proportion / 100)

                    elif result > 0:
                        proportion = abs(result) / (int(self.employees[i][-4:]) / 100)
                        salary = int(self.employees[i][20:26]) + (int(self.employees[i][20:26]) * proportion / 100)

                    else:
                        salary = int(self.employees[i][20:26])
                    print(self.employees[i].rstrip("\n") + "{:>17} {:>18}".format(int(self.work_hours[j][-4:]),
                                                                                  int(salary)))


employ = Employee()
employ.payroll()
