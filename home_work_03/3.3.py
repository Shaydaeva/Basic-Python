def my_func(a, b, c):
    """Возвращает сумму двух наибольших"""
    num = [a, b, c]  # Список из аргументов
    num.remove(min(num))  # Удаляет min значение
    return sum(num)


print(my_func(6, 2, 8))
