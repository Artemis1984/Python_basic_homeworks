# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    str_ticket = str(ticket_number)
    if str_ticket[0] == str_ticket[len(str_ticket)-1]:
        return "Билет счастливый!"
    else:
        return "Билет не счастливый!"


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436754))



