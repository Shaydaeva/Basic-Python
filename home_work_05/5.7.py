import json

comp_dict = {}  # Для фирм и прибыли

with open("text_7.txt", encoding='utf-8') as f_obj:
    """Читаем файл построчно, фирму с прибылью
       (в т.ч. отрицательной). В цикле сбор данных для
       расчета средней прибыли без учета убыточных компаний"""
    res_prof = 0
    count = 0
    for line in f_obj:
        prof = int(line.split()[2]) - int(line.split()[3])
        comp_dict[line.split()[0]] = prof
        if prof > 0:
            res_prof += prof
            count += 1

# Расчет средней прибыли
average_profit = dict(average_profit=(res_prof // count))

# Формирование списка
prof_comp = [comp_dict, average_profit]
print(prof_comp)

# Сохранение в виде json-объекта
with open("my_json.json", "w", encoding='utf-8') as f:
    json.dump(prof_comp, f, ensure_ascii=False, indent=4)
