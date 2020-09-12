# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("work4.txt", "r", encoding='utf-8') as file1:
    for i in file1:
        new_txt = ""
        for el in i.split():
            if el in my_dict.keys():
                ru_text = my_dict[el]
                new_txt += ru_text
            else:
                new_txt += ' ' + el
        new_txt += "\n"
        with open("work4_2.txt", "a", encoding='utf-8') as file2:
            file2.write(new_txt)