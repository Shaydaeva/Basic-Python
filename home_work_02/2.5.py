my_list = [7, 5, 3, 3, 2]

rat = int(input('Вводим рейтинг: '))

if rat > 0:
    if rat in set(my_list):
        for el in set(my_list):
            if rat == el:
                my_list.insert(my_list.index(el) + my_list.count(el), rat)
                break
    else:
        for el in my_list:
            if rat > el:
                my_list.insert(my_list.index(el), rat)
                break
        if rat not in set(my_list):
            my_list.append(rat)
    print(my_list)
else:
    print('Необходимо внести целое положительное число')


