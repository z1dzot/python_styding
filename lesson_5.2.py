# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

lines = 0
words = 0
symbols = 0

with open('test_2.txt', 'r') as my_f:
    for line in my_f:
        lines += 1
        symbols += len(line)

        pos = 'out'
        for symbol in line:
            if symbol != ' ' and pos == 'out':
                words += 1
                pos = 'in'
            elif symbol == ' ':
                pos = 'out'


print(lines)
print(words)
print(symbols)

