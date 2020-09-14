# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула(куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


import random

turnlist = ["направо", "налево"]

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f"Машина {self.name}, {self.color} цвета начала движение")

    def turn(self, direction):
        if direction == "направо":
            print("Машина повернула направо")
        else:
            print("Машина повернула налево")

    def show_speed(self):
        print(f"Скорость автомобиля {self.speed}")

    def stop(self):
        print(f"Машина {self.name}, {self.color} цвета остановилась")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость автомобиля {self.speed}")
            print(f'Скорость превышена на {self.speed - 60}')
        else:
            print(f"Скорость автомобиля {self.speed}")


class SportCar(Car):
    def show_sportcar(self):
        print(f'Спортивная машина:')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость автомобиля {self.speed}")
            print(f'Скорость превышена на {self.speed - 40}')
        else:
            print(f"Скорость автомобиля {self.speed}")


class PoliceCar(Car):
    def show_policecar(self):
        self.is_police = True


car1 = TownCar(random.randint(60, 100), "Чёрного", 'Kia')
car1.go()
car1.turn(random.choice(turnlist))
car1.show_speed()
car1.stop()
print(f'полицейкая машина - {car1.is_police}')
print("")

car2 = SportCar(random.randint(0, 100), "Красного", "Ferrari")
car2.show_sportcar()
car2.go()
car2.turn(random.choice(turnlist))
car2.show_speed()
car2.stop()
print(f'полицейкая машина - {car2.is_police}')
print("")

car3 = WorkCar(random.randint(40, 100), "Синего", "Ducato")
car3.go()
car3.turn(random.choice(turnlist))
car3.show_speed()
car2.stop()
print(f'полицейкая машина - {car3.is_police}')
print("")

car4 = PoliceCar(random.randint(0, 100), "Сине-белого", "Ваз 2109")
car4.show_policecar()
car4.go()
car4.turn(random.choice(turnlist))
car4.show_speed()
car4.stop()
print(f'полицейкая машина - {car4.is_police}')
