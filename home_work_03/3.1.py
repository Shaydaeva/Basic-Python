def div(a, b):
    try:
        print(f"{float(a) / float(b):.2f}")
    except ValueError:
        print("Нужно было ввести число")
    except ZeroDivisionError:
        print("Делить на ноль нельзя")


div(input("Введите делимое: "), input("Введите делитель: "))
