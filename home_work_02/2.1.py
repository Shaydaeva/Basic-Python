my_list = [None, 9, 7.3, (3 + 2j), 'qwe', [2, 3],
           ('name', 'age'), {73, 25, 31},
           {1: 'a', 2: 'b'}, False, b'text']

for el in my_list:
    print(f"{str(el):<20} - {str(type(el)):>20}")
