# Поработайте с переменными, создайте несколько, выведите на экран, запросите у
# пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

first_num = 1
second_num = 20

print(first_num, second_num)


print("------------------------")


user_number1 = int(float(input("Введите целое число: ")))
user_number2 = float(input("Введите десятичное число: "))
user_str1 = input("Введите любой текст: ")
user_str2 = input("И еще раз: ")


print("%d %d %s %s" % (user_number1, user_number2, user_str1, user_str2))


