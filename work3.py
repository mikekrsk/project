# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


month = int(input("Введите месяц в виде числа от 1 до 12: "))
some_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
if month in some_list[0]:
    print("list зима")
elif month in some_list[1]:
    print("list весна")
elif month in some_list[2]:
    print("list лето")
elif month in some_list[3]:
    print("list осень")
else:
    print("Вы ввели что то не то")

# Через dict

my_dict = {"dict зима": [1, 2, 12], "dict весна": [3, 4, 5], "dict лето": [6, 7, 8], "dict осень": [9, 10, 11]}
for key, val in my_dict.items():
    if month in val:
        print(key)
