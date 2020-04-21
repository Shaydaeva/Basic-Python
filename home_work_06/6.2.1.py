class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        mass = 25
        thickness = 5
        result = self._length * self._width * mass * thickness // 1000
        print(f"Необходимо {result} тонн асфальтного покрытия")

try:
    first_road = Road(int(input("Длина дороги в метрах: ")),
                      int(input("Ширина дороги в метрах: ")))
    first_road.calc_mass()
except ValueError:
    print("Incorrect values. Only numbers")
