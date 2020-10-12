# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_function(num1, num2, num3):
    if num1 >= num3 and num2 >= num3:
        return num1 + num2
    elif num1 > num2 and num2 < num3:
        return num1 + num3
    else:
        return num2 + num3


print(
    f'Result: {my_function(int(input("Enter number 1: ")), int(input("Enter number 2: ")), int(input("Enter number 3: ")))}')


### Подглядел в инете такой вариант, оч понравился, оставлю тут

# def my_func(x, y, z):
#     sequence = [x, y, z]
#     total = []
#     max_1 = max(sequence)
#     total.append(max_1)
#     sequence.remove(max_1)
#     max_2 = max(sequence)
#     total.append(max_2)
#     print(sum(total))
#
#
# my_func(-4, 2, 0)
