# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def two_num(num_1, num_2):
    try:
        divide = num_1 / num_2
    except ZeroDivisionError:
        print("Деление на 0!")
        return
    else:
        print(divide)


num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
two_num(num_1, num_2)
