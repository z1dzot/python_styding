# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def function(var1, var2):
    try:
        var = var1 / var2
        return var
    except ZeroDivisionError:
        return "var2 not a zero. Enter only number!"


print(function(int(input("Enter var1 = ")), int(input("Enter var2 = "))))
