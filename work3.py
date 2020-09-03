# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def sum_twomax(num_1, num_2, num_3):
    user_list = [num_1, num_2, num_3]
    user_list.remove(min(user_list))
    return sum(user_list)


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))


print(f"{'Сумма наибольших двух аргументов:'} {sum_twomax(num_1, num_2, num_3)}")


# def sum_twomax(num_1, num_2, num_3):
#     list = [num_1, num_2, num_3]
#     list.sort()
#     summa = list[-1] + list[-2]
#     return summa
#
# print("Сумма наибольших двух аргументов: " + str(sum_twomax(int(input("Введите первое число: ")),
#                  int(input("Введите второе число: ")), int(input("Введите третье число: ")))))


