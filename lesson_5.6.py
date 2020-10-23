# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
# по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

my_dict = {}
with open("task_6.txt", encoding='utf-8') as f_o:
    for line in f_o:
        name, stats = line.split(":")
        name_sum = sum(map(int, "".join([i for i in stats if i == " " or i.isdigit()]).split()))
        my_dict[name] = name_sum
print(my_dict)

# ВТОРОЙ СПОСОБ
print("\n***********SECOND WAY**************\n")
with open("task_6.txt", "r", encoding='utf-8') as t_o:
    lines = t_o.readlines()
    for line in lines:
        new_str = "".join((i if i in "1234567890" else " ") for i in line)
        new_2 = [int(i) for i in new_str.split()]
        print(f"{line.split()[0]} {sum(new_2)}")
