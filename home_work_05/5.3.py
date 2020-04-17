list_emp = []  # Для списка сотрудников
count = 0
am = 0

with open("text_3.txt", encoding='utf-8') as f_obj:
    for line in f_obj:
        list_emp.append(line.split())

print("Список сотрудников с окладом менее 20 тыс.:")
for i in list_emp:
    i[1] = float(i[1])
    if i[1] < 20000:
        print(i[0])
    am += i[1]
    count += 1

print(f"\nСредний доход сотрудников - {am/count:.2f}")
