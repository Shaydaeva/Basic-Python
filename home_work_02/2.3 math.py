month = int(input('Введите порядковый номер месяца(от 1 до 12): '))

if 1 <= month <= 12:
    if 3 <= month <= 5:
        print('Весна')
    elif 6 <= month <= 8:
        print('Лето')
    elif 9 <= month <= 11:
        print('Осень')
    else:
        print('Зима')
else:
    print('Такого месяца не существует')
