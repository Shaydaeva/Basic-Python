class MyExcError(Exception):
    def __init__(self, txt):
        self.txt = txt


def multisum():
    """Немного усовершенствованный вариант"""
    print("Введите строку чисел, разделенных пробелом, спецсимвол для подсчета итога - &")
    total_sum = []
    while True:
        user_sec = input("Введите числа: ").split()
        try:
            for i in user_sec:
                if i == '&':
                    continue
                elif not i.isdigit():
                    raise MyExcError("Введены некорректные значения.")
        except MyExcError as err:
            print(err)
            continue
        if '&' in user_sec:
            for i in range(user_sec.index('&')):
                total_sum.append(int(user_sec[i]))
            break
        else:
            for i in user_sec:
                total_sum.append(int(i))
    print(total_sum)


multisum()
