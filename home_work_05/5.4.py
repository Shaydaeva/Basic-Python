"""Возьмет только слова из словаря"""

trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("text_4.txt", encoding='utf-8') as f_eng:
    with open("my_4_rus.txt", "w", encoding='utf-8') as f_rus:
        for line in f_eng:
            new_list = list(line.partition(' - '))
            new_list[0] = trans.get(new_list[0])
            f_rus.write(''.join(new_list))
