row = 0  # Счетчик строк
word = 0  # Счетчик слов

with open("my_2.txt", encoding='utf-8') as file:
    for i, line in enumerate(file, 1):
        row += 1
        word += len(line.split())
        print(f"{i} строка слов - {len(line.split())}")

print(f"\nВсего строк {row}. Всего слов - {word}")
