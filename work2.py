# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def my_method_1(self):
        pass

    @abstractmethod
    def my_method_2(self):
        pass


class Сlothes(MyAbstractClass):
    def __init__(self, size, height):
        self.size = size
        self.height = height
    @property
    def my_method_1(self):
        resultcoat = (self.size / 6.5 + 0.5)
        return resultcoat
    @property
    def my_method_2(self):
        resultsuit = (2 * self.height + 0.3)
        return resultsuit
    @property
    def total_expense(self):
        resultall = self.my_method_1 + self.my_method_2
        return resultall


mc = Сlothes(6.5, 10)
print("Расход ткади для пальто: {:.2f}".format(mc.my_method_1) + " m")
print("Расход ткади для костюма: {:.2f}".format(mc.my_method_2) + " m")
print("Общий расход ткани: {:.2f}".format(mc.total_expense) + " m")