my_list = list((input('Введите список: ')).replace(',', ' ').split())

for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(my_list)
