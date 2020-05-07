class IncorrInput(Exception):
    """Ввод некорректного значения"""
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    """Класс склад. Реализация приёма техники и перемещения в подразделения"""
    equip_list = {1: 'принтер', 2: 'сканер', 3: 'ксерокс'}  # Словарь id: тип техники
    avail_store = {equip_list.get(1): {}, equip_list.get(2): {}, equip_list.get(3): {}}  # Наличие на складе
    company = {1: 'Главный офис', 2: 'Центр продаж', 3: 'Аналитический центр'}  # Словарь id: название подразделения
    # Наличие в подразделениях
    equip_company = {company.get(1): {equip_list.get(1): {}, equip_list.get(2): {}, equip_list.get(3): {}},
                     company.get(2): {equip_list.get(1): {}, equip_list.get(2): {}, equip_list.get(3): {}},
                     company.get(3): {equip_list.get(1): {}, equip_list.get(2): {}, equip_list.get(3): {}}}

    @staticmethod
    def add_equip_to_store(equip):
        """Добавление техники на склад с проверкой, если модель уже существует, то добавить количество"""
        value_list = equip.data_input()  # Список из инита оргтехники
        #  Проверка наличия такого типа техники
        if (value_list[0], value_list[1]) in Warehouse.avail_store.get(equip._name):
            Warehouse.avail_store.get(equip._name)[(value_list[0], value_list[1])] = \
                Warehouse.avail_store.get(equip._name).get((value_list[0], value_list[1])) + value_list[2]
        else:
            Warehouse.avail_store.get(equip._name)[(value_list[0], value_list[1])] = value_list[2]

    @staticmethod
    def reception():
        """Приём техники на склад"""
        print("Приём оргтехники по номеру в списке. "
              "Для выхода из меню приёма введите q")
        while True:
            user_input = input(f"1 - {Warehouse.equip_list.get(1)}\n"
                               f"2 - {Warehouse.equip_list.get(2)}\n"
                               f"3 - {Warehouse.equip_list.get(3)}\n"
                               f"Для выхода введите q\nВвод: ")
            if user_input == 'q':  # Проверка на символ выхода
                break
            try:
                # Проверка ввода на число и принадлежность к id словаря по типу техники, перехват исключений
                if not user_input.isdigit() or int(user_input) not in Warehouse.equip_list.keys():
                    raise IncorrInput("Ввод некорректного значения")
                # Число - тип техники, работа со словарем по ключу на складе
                choice_class = {1: Printer, 2: Scanner, 3: Copier}
                Warehouse.add_equip_to_store(choice_class.get(int(user_input)))
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
            user_input = input(f"Выберите категорию:\n1 - {Warehouse.equip_list.get(1)}\n"
                               f"2 - {Warehouse.equip_list.get(2)}\n"
                               f"3 - {Warehouse.equip_list.get(3)}\n"
                               f"Для выхода введите q\nВвод: ")
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
                company_input = int(input(f"Выберите подразделение:\n1 - {Warehouse.company.get(1)}\n"
                                          f"2 - {Warehouse.company.get(2)}\n"
                                          f"3 - {Warehouse.company.get(3)}\n"
                                          f"Для выхода введите q\nВвод: "))
                if company_input not in Warehouse.company.keys():
                    print("\nТакого подразделения не существует\n")
                    continue
            except ValueError:
                print("\nВведено некорректное значение. Повторите ввод.")
                continue
            type_equip = Warehouse.equip_list.get(int(user_input))  # Значение по ключу id, получим тип техники
            # Промежуточный список выбранного типа техники. Значение по ключу тип техники, список на складе
            store_interim_dict = Warehouse.avail_store.get(type_equip)
            comp_interim_dict = Warehouse.equip_company.get(Warehouse.company.get(int(company_input))).get(type_equip)
            # Если позиция по ключу существует, доступен выбор позиций
            if store_interim_dict:
                new_interim_dict = {}
                count = 0
                for k, v in store_interim_dict.items():
                    count += 1
                    new_interim_dict[count] = (k, v)
                for i in new_interim_dict.items():
                    print(i)
            else:
                print("\nТовара нет на складе\n")
                continue
            try:
                index_element = int(input('Введите номер: '))  # Ключ interim_dict
                if index_element not in new_interim_dict.keys():
                    print("\nЭлемента не существует\n")
                    continue
                quan_input = int(input("Введите количество: "))  # Сколько перевести в подразделение
                if quan_input < 1:
                    print('Количество может быть только положительным числом')
                    continue
            except ValueError:
                print("Необходимо ввести число")
                continue
            except TypeError:
                print("Введено некорректное значение")
                continue
            # Проверка наличия необходимого количества на складе
            unit = new_interim_dict.get(index_element)[0]  # [0] - Ключ (фирма и модель), [1] - количество
            if new_interim_dict.get(index_element)[1] < quan_input:
                print("Введенное количество больше имеющегося на складе.")
                continue
            elif new_interim_dict.get(index_element)[1] == quan_input:
                # Удаление по ключу из склада. Добавление в список подразделений
                comp_interim_dict[unit] = store_interim_dict.pop(unit)
            else:
                # Уменьшает количество на складе, увеличивает в подразделении
                store_interim_dict[unit] = store_interim_dict.get(unit) - quan_input
                if unit in comp_interim_dict.keys():
                    comp_interim_dict[unit] = comp_interim_dict.get(unit) + quan_input
                else:
                    comp_interim_dict[unit] = quan_input
        return "\nВсе данные внесены\n"  # Warehouse.company, Warehouse.avail_store

    @staticmethod
    def report():
        """Отчет по окончанию приёма и отправки в подразделения"""
        print("\nТехника на складе:")
        for k, v in Warehouse.avail_store.items():
            if v:
                print(f"{k}:")
            for i, j in v.items():
                print(f"{i[0]:>10} {i[1]:>10} {j:>5} шт")
        print("\nТехника в подразделениях:")
        for k, v in Warehouse.equip_company.items():
            print(k)
            for i, j in v.items():
                if j:
                    print(i)
                for a, b in j.items():
                    print(f"{a[0]:>15} {a[1]:>10} {b:>5} шт")
        return '\n'


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
    _name = Warehouse.equip_list.get(1)


class Scanner(OffEquip):
    _name = Warehouse.equip_list.get(2)


class Copier(OffEquip):
    _name = Warehouse.equip_list.get(3)


while True:
    user_input = input("Главное меню. Выберите действие:\n"
                       "1 - Приём на склад\n"
                       "2 - Передача в подразделение\n"
                       "3 - Просмотр отчета\n"
                       "Для выхода введите exit\n>>> ")
    try:
        if user_input == 'exit':
            print("Завершение работы программы")
            break
        elif int(user_input) == 1:
            print(Warehouse.reception())
        elif int(user_input) == 2:
            print(Warehouse.transfer())
        elif int(user_input) == 3:
            print(Warehouse.report())
        else:
            print("\nВведите число из предложенных\n")
            continue
    except ValueError:
        print("\nВведите число из предложенных\n")
        continue
