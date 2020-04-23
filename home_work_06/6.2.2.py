class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, mass, thickness):
        result = self._length * self._width * mass * thickness // 1000
        print(f"Необходимо {result} тонн асфальтного покрытия")


try:
    first_road = Road(int(input("Длина дороги в метрах: ")),
                      int(input("Ширина дороги в метрах: ")))
    first_road.calc_mass(int(input("Масса 1кв.м. асфальта толщиной 1 см в кг: ")),
                         int(input("Толщина покрытия в см: ")))
except ValueError:
    print("Incorrect values. Only numbers")
