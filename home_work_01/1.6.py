a = int(input("Результат первого дня: "))
b = int(input("Цель: "))
day = 1

if a > b or a < 0:
    print("Введены некорректные данные")
else:
    while a < b:
        a = a * 1.1
        day += 1

    print(f"На {day} день спортсмен достигнет результата - не менее {b} км.")