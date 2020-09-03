# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def tel_book(name, surname, year, city, email, tel):
    print("Имя: " + name, "Фамилия: " + surname, "Год рождения: " + str(year),
          "Город проживания: " + city, "email: " + email, "Телефон: " + str(tel), sep=', ')


try:
    name = input("name: ").title()
    surname = input("surname: ").title()
    year = int(input("year of birth: "))
    city = input("сity of residence: ").title()
    email = input("email: ")
    tel = int(input("telephon: "))
except ValueError:
    print("Введите год рождения и телефон числом")
else:
    tel_book(name=name, year=year, surname=surname, city=city, email=email, tel=tel)
