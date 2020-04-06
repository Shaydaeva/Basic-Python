month = int(input('Введите порядковый номер месяца(от 1 до 12): '))

season = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5],
      'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

if 1 <= month <= 12:
    for k,v in season.items():
        for i in v:
            if month == i:
                print(k)
else:
    print('Такого месяца не существует')
