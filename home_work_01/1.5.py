comp_rev = int(input("Введите сумму выручки компании: "))
comp_costs = int(input("Введите сумму издержек компании: "))

if comp_rev > comp_costs:
    profit = comp_rev - comp_costs # прибыль
    rent = profit / comp_rev * 100 # рентабельность в %
    print(f"Прибыль компании {profit} у.е.!\nРентабельность составила {rent:.2f}%")
    num_emp = int(input("Укажите численность сотрудников компании: "))
    prof_per_emp = profit / num_emp # прибыль на одного сотрудника
    print(f"Прибыль в расчете на одного сотрудника составила {prof_per_emp:.2f} у.е.")
elif comp_rev == comp_costs:
    print("Вы работаете 'в ноль'")
else:
    print(f"Вы работаете в убыток.\nУбыток составил {comp_costs - comp_rev} у.е.")

