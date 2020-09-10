# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


with open('work1.txt', 'w') as f:
    while True:
        user_text = input("Введите данные: ")
        if not user_text:
            break
        else:
            print(user_text, file=f)
