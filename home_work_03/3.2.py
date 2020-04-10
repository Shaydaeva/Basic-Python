def user(first_name, last_name, year_birth, city,
         email='<не указан>', phone_number='<не указан>'):
    """Возващает данные пользователя"""
    print(first_name, last_name, year_birth, city, email, phone_number)


# Ввод данных пользователя для функции
first_name = input("Ваше имя: ").capitalize()
last_name = input("Ваше фамилия: ").capitalize()
year_birth = input("Год рождения: ")
city = input("Город: ").capitalize()
email = input("Email: ")
phone_number = input("Номер телефона: ")

user(first_name, last_name, year_birth, city)
