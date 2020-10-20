# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

from statistics import mean

salaries = []
with open("test_3.txt") as workers:
    for worker in workers:
        last_name, salary = worker.split()
        salary = int(salary)
        if salary < 20000:
            print(last_name)
            salaries.append(salary)

print(f'Mid salary: {mean(salaries):.2f}')


