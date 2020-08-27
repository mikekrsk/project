# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число: "))
maximum = 0
while number != 0:
    a = number % 10
    number //= 10
    if a > maximum:
        maximum = a
    elif maximum == 9:
        break
    else:
        continue
print('Самая большая цифра в числе: ', maximum)
