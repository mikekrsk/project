# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

firm_list = []
with open('work7.txt', "r", encoding='utf-8') as f_obj:
    for i in f_obj.readlines():
        firm_list.append([i.split()[0], float(i.split()[-2]) - float(i.split()[-1])])

profit_list = [i[-1] for i in firm_list if i[-1] > 0]

final_list = [{firm_list[i][0]: round(firm_list[i][-1], 2) for i in range(len(firm_list))},
              {"average_profit": round(sum(profit_list) / len(profit_list), 2)}]

print(final_list)

with open('work7.json', 'w', encoding='utf-8') as write_json:
    json.dump(final_list, write_json)
