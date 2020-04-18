study_dict = {}  # Словарь для результата

with open("text_6.txt", encoding='utf-8') as file_st:
    """Читаем построчно файл, данные до : в ключ,
       '-' пропускаем, после : и до скобки суммируем
       и добавляем в значение по ключу"""
    for line in file_st:
        res = 0
        for i in line[line.find(':')+1:].split():
            if i == '-':
                continue
            else:
                res += int(i[:i.find('(')])
        study_dict[line[:line.find(':')]] = res


for k, v in study_dict.items():
    print(f"{k:<15} - {v:>4}")
