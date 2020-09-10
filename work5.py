# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

with open('work5.txt', 'w') as f:
    for el in my_list:
        f.write(str(el) + ' ')

with open('work5.txt', 'r') as f:
    user_list = [int(el) for el in f.read().split()]

print(sum(user_list))
