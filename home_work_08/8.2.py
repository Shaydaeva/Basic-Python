class MyZeroDevError(Exception):
    def __init__(self, txt):
        self.txt = txt


class TooMany(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_dev = input("Введите выражение деления: ")

try:
    dev_list = inp_dev.split('/')
    if len(dev_list) > 2:
        raise TooMany("Введено больше действий")
    for i in range(len(dev_list)):
        dev_list[i] = int(dev_list[i])
    if dev_list[1] == 0:
        raise MyZeroDevError("Ошибка деление на ноль")
except MyZeroDevError as zero_err:
    print(zero_err)
except TooMany as many:
    print(many)
except ValueError:
    print("Выражение введено некорректно")
else:
    print(f"{dev_list[0] / dev_list[1]:.3f}")
