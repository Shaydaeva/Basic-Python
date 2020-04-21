from random import choice
from random import randint


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Created a {self.name} {'police ' if self.is_police else ''}car in {self.color}")

    def go(self):
        print(f"{self.name} started")

    def stop(self):
        print(f"{self.name} stopped")

    def turn(self):
        dir_turn = ['left', 'right', 'around']
        for i in range(randint(3, 10)):
            print(f"{self.name} turned {choice(dir_turn)}")

    def show_speed(self):
        print(f"For {self.name} speed {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"For {self.name} OVER SPEED ! ! ! more than 60")
        else:
            Car.show_speed(self)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"For {self.name} OVER SPEED ! ! ! more than 40")
        else:
            Car.show_speed(self)


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


#  Функция работает, пока названия всех методов одинаковые
def moving_car(name):
    name.go()
    name.show_speed()
    name.turn()
    name.stop()
    print('\n')

#  Создание машин и обработка действий с помощью функции
town_car_1 = TownCar(50, 'red', 'Lada')
moving_car(town_car_1)

town_car_2 = TownCar(70, 'argent', 'Mersedes')
moving_car(town_car_2)

work_car_1 = WorkCar(30, 'white', 'Mazda')
moving_car(work_car_1)

work_car_2 = WorkCar(50, 'black', 'Lexus')
moving_car(work_car_2)

sport_car_1 = SportCar(120, 'green', 'Audi')
moving_car(sport_car_1)

sport_car_2 = SportCar(150, 'orange', 'Corvette')
moving_car(sport_car_2)

police_car_1 = PoliceCar(80, 'white', 'Ford', True)
moving_car(police_car_1)

police_car_2 = PoliceCar(60, 'blue', 'Volvo', True)
moving_car(police_car_2)

"""Ну и конечно не могла не попробовать со словарем)) Только создание машин происходит сразу всех.
   Места занимает меньше, выглядит вроде красиво, не знаю насколько применимо в жизни"""
# all_cars = {'town_car_1': TownCar(50, 'red', 'Lada'),
#             'town_car_2': TownCar(70, 'argent', 'Mersedes'),
#             'work_car_1': WorkCar(30, 'white', 'Mazda'),
#             'work_car_2': WorkCar(50, 'black', 'Lexus'),
#             'sport_car_1': SportCar(120, 'green', 'Audi'),
#             'sport_car_2': SportCar(150, 'orange', 'Corvette'),
#             'police_car_1': PoliceCar(80, 'white', 'Ford', True),
#             'police_car_2': PoliceCar(60, 'blue', 'Volvo', True)}
#
# for i in all_cars:
#     moving_car(all_cars.get(i))
