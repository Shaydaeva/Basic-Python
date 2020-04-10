def my_func():
    """Возводит в отрицательную степень"""
    try:
        x = float(input("Введите действительное положительное число: "))
        y = int(input("Введите целое отрицательное число: "))
        if x > 0 and y < 0:  # Проверка условий
            pow_x = 1
            for i in range(abs(y)):
                pow_x = pow_x * x
            return f"{1 / pow_x:.5f}"
        else:
            return "Введены числа не удовлетворяющие условиям."
    except ValueError:
        return "Введены значения не удовлетворяющие условиям."


print(my_func())
