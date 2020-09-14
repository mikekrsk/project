# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

user_dict = {"wage": 10, "bonus": 20}


class Worker:
    name = ""
    surname = ""
    position = ""
    _income = user_dict


class Position(Worker):
    def get_total_income(self):
        print(f'Доход с учётом премии: {sum(self._income.values())}р')
        pass

    def get_full_name(self):
        print(f'Полное имя: {self.name} {self.surname}. Должность: {self.position}')
        pass

attribute = Position()
attribute.name = "Василий"
print(attribute.name)
attribute.surname = "Петров"
print(attribute.surname)
attribute.position = "Директор"
print(attribute.position)
attribute.get_full_name()
attribute.get_total_income()
