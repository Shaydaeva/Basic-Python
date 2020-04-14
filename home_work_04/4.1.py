from sys import argv

script_name, prod, rate, bonus = argv

try:
    salary = float(prod) * float(rate) + float(bonus)
    print("Выработка часов - ", prod,
          "\nСтавка - ", rate,
          "\nПремия - ", bonus,
          "\nЗаработная плата - ", salary)
except ValueError:
    print("Введены некорректные значения")
