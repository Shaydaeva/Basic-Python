answer = 'да'
count = 0
product_list = []
product_dict = {'название': list(), 'цена': list(), 'количество': list(), 'ед': list()}

while answer != 'нет':
    count += 1
    title = input('Название: ').lower()
    price = int(input('Цена: '))
    quan = int(input('Количество: '))
    unit = input('Единица измерения: ').lower()
    product_dict['название'].append(title)
    product_dict['цена'].append(price)
    product_dict['количество'].append(quan)
    if unit not in product_dict.get('ед'):
        product_dict['ед'].append(unit)
    product_list.append((count, {'название': title, 
                                 'цена': price, 
                                 'количество': quan,
                                 'ед': unit}))
    answer = input('Продолжить? да\нет ').lower()
    
all_list = input('Вывести список товаров? да\нет ')
if all_list == 'да':
    for el in range(len(product_list)):
        print(product_list[el])

rep = input('Вывести анализ? да\нет ')
if rep == 'да':
    for el in product_dict.items():
        print(el)
    
