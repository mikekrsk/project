# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


user_input = input("Введите список элементов через пробел: ").split()

i = 0
for el in range(int(len(user_input) / 2)):
    user_input[i], user_input[i + 1] = user_input[i + 1], user_input[i]
    i += 2
print(user_input)
