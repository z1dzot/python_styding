# Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv

file_name, work_per_hour, rate, prize = argv

salary = (int(work_per_hour) * int(rate)) + int(prize)

print(f'Your salary: {salary}')

