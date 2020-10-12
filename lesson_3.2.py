# Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def info(**kwargs):
    return kwargs


print(f'first_name = {input("Enter your name: ")}; last_name = {input("Enter your last name: ")};'
      f'b_year = {input("Enter ur birth date: ")}; city = {input("City u live: ")};'
      f'email = {input("email address: ")}; phone_number = {int(input("Phone number: "))}')
