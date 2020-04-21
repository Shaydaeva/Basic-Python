class Worker:
    """Создание базового класса"""

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    """Дочерний класс с методами рассчета"""

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        try:
            income_res = int(self._income.get('wage')) + int(self._income.get('bonus'))
            print(f"{income_res}")
        except ValueError:
            print("Введены некорректные значения оклада и/или премии")

# Создание объектов
# person_1 = Position('Ivan', 'Ivanov', 'manager', 50000, 10000)
# person_2 = Position('Петр', 'Петров', 'инженер', 70000, 20000)
# person_3 = Position('Anna', 'Novikova', 'clerk', 30000, 30000)

# Вызовы методов для каждого объекта
# person_1.get_full_name()
# person_1.get_total_income()
# person_2.get_full_name()
# person_2.get_total_income()
# person_3.get_full_name()
# person_3.get_total_income()

#  Решила попробовать так и получилось)
person_list = {'person_1': Position('Ivan', 'Ivanov', 'manager', 50000, 10000),
             'person_2': Position('Петр', 'Петров', 'инженер', 70000, 20000),
             'person_3': Position('Anna', 'Novikova', 'clerk', 30000, 30000)}

def output(person):
    return person.get_full_name(), person.get_total_income()

for i in person_list:
    output(person_list.get(i))
