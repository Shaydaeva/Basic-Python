from random import randint


with open("my_5.txt", "w+") as f_obj:
    f_obj.write(' '.join(str(i) for i in [randint(1, 100) for i in range(randint(5, 15))]))
    f_obj.seek(0)
    res = 0
    for i in f_obj.read().split():
        res += int(i)
    print("Сумма чисел в файле: ", res)
