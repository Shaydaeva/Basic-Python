def multisum():
    """Немного усовершенствованный вариант"""
    print("Введите строку чисел, разделенных пробелом, спецсимвол для подсчета итога - &")
    total_sum = 0
    while True:
        user_sec = input("Введите числа: ").split()
        try:
            for i in user_sec:
                if i == '&':
                    continue
                else:
                    int(i)
        except ValueError:
            print("Введены некорректные значения.")
            continue
        if '&' in user_sec:
            for i in range(user_sec.index('&')):
                total_sum += int(user_sec[i])
            print("Общая сумма = ", total_sum)
            break
        else:
            for i in user_sec:
                total_sum += int(i)
            print(total_sum)


multisum()
