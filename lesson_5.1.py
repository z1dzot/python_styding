# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

my_file = input('Назовите файл в расширении .txt: ')
open_file = open(my_file, 'w')

while True:
    line = input('Введите текст в файл: ')
    if line == ' ':
        break
    open_file.write(line + '\n')

open_file.close()


