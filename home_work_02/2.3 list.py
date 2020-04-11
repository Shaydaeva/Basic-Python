month = int(input('Введите порядковый номер месяца(от 1 до 12): '))

season = [[[12, 1, 2], 'Зима'], [[3, 4, 5], 'Весна'],
          [[6, 7, 8], 'Лето'], [[9, 10, 11], 'Осень']]

if 1 <= month <= 12:
    for el in range(len(season)):
        for i in season[el][0]:
            if month == i:
                print(season[el][1])
else:
    print('Такого месяца не существует')
