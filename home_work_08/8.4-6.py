class IncorrInput(Exception):
    """Ввод некорректного значения"""
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    """Класс склад. Реализация приёма техники и перемещения в подразделения"""
    equip_list = {1: 'принтер', 2: 'сканер', 3: 'ксерокс'}  # Словарь id: тип техники
    avail_store = {'принтер': [], 'сканер': [], 'ксерокс': []}  # Наличие на складе
    company = {'Главный офис': {'принтер': [], 'сканер': [], 'ксерокс': []},
               'Центр продаж': {'принтер': [], 'сканер': [], 'ксерокс': []},
               'Аналитический центр': {'принтер': [], 'сканер': [], 'ксерокс': []}}  # Наличие в подразделениях

    @staticmethod
    def reception():
        """Приём техники на склад"""
        print("Приём оргтехники по номеру в списке. "
              "Для выхода из меню приёма введите q")
        while True:
            user_input = input("1 - принтер\n2 - сканер\n3 - ксерокс\n"
                               "Для выхода введите q\nВвод: ")
            if user_input == 'q':  # Проверка на символ выхода
                break
            try:
                # Проверка ввода на число и принадлежность к id словаря по типу техники, перехват исключений
                if not user_input.isdigit() or int(user_input) not in Warehouse.equip_list.keys():
                    raise IncorrInput("Ввод некорректного значения")
                # Число - тип техники, добавление списка по ключу на склад
                if int(user_input) == 1:
                    Warehouse.avail_store.get(Printer._name).append(Printer.data_input())
                elif int(user_input) == 2:
                    Warehouse.avail_store.get(Scanner._name).append(Scanner.data_input())
                elif int(user_input) == 3:
                    Warehouse.avail_store.get(Copier._name).append(Copier.data_input())
            except IncorrInput as ii:
                print(ii)
                continue
            except ValueError:
                print("Количество может быть только целым числом. Повторите ввод.")
                continue
        return "\nОкончание приёма оргтехники"  # Warehouse.avail_store

    @staticmethod
    def transfer():
        """Передача техники со склада в подразделение"""
        print("\nПередача техники в подразделение.\n")
        while True:
            #  Что передаём, с перехватом исключений
            user_input = input("Выберите категорию:\n1 - принтер\n2 - сканер\n3 - ксерокс\n"
                               "Для выхода введите q\nВвод: ")
            if user_input == 'q':
                break
            try:
                if not user_input.isdigit() or int(user_input) not in Warehouse.equip_list.keys():
                    raise IncorrInput("\nВведено некорректное значение")
            except IncorrInput as ii:
                print(ii)
                continue
            try:
                #  Куда передаём, с перехватом исключений
                company_input = int(input("Выберите подразделение:\n1 - Главный офис\n2 - Центр продаж\n"
                                          "3 - Аналитический центр\nДля выхода введите q\nВвод: "))
            except ValueError:
                print("\nВведено некорректное значение. Повторите ввод.")
                continue
            #  Промежуточный список выбранного типа техники
            type_equip = Warehouse.equip_list.get(int(user_input))  # Значение по ключу id, получим тип техники
            # Значение по ключу тип техники, получим позиции на складе
            interim_list = Warehouse.avail_store.get(type_equip)
            # Если позиция по ключу существует, доступен выбор позиций
            if interim_list:
                for id, el in enumerate(interim_list, 1):
                    print(id, el)
            else:
                print("\nТовара нет на складе\n")
                continue
            index_element = int(input('Введите номер: ')) - 1  # Индекс элемента в списке
            # Удаление по индексу из склада. Добавление в список подразделений
            if int(company_input) == 1:
                Warehouse.company.get('Главный офис')[type_equip].append(interim_list.pop(index_element))
            elif int(company_input) == 2:
                Warehouse.company.get('Центр продаж')[type_equip].append(interim_list.pop(index_element))
            elif int(company_input) == 3:
                Warehouse.company.get('Аналитический центр')[type_equip].append(interim_list.pop(index_element))
        return "\nВсе данные внесены. Вывод отчета при окончании работы"  # Warehouse.company, Warehouse.avail_store

    @staticmethod
    def report():
        """Отчет по окончанию приёма и отправки в подразделения"""
        print("\nТехника на складе:")
        for k, v in Warehouse.avail_store.items():
            print(k, v)
        print("\nТехника в подразделениях:")
        for k, v in Warehouse.company.items():
            print(k, v)
        return "\nЗавершение работы программы"


class OffEquip:

    def __init__(self, manufacturer, model, quantity):
        self.manufacturer = manufacturer
        self.model = model
        self.quantity = quantity

    @staticmethod
    def data_input():
        OffEquip.manufacturer = input("Производитель: ")
        OffEquip.model = input("Модель: ")
        OffEquip.quantity = int(input("Количество: "))
        return [OffEquip.manufacturer, OffEquip.model, OffEquip.quantity]


class Printer(OffEquip):
    _name = 'принтер'


class Scanner(OffEquip):
    _name = 'сканер'


class Copier(OffEquip):
    _name = 'ксерокс'


print(Warehouse.reception())
print(Warehouse.transfer())
print(Warehouse.report())
