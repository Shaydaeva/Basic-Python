""" Можно запрашивать название файла у пользователя,
    в моём случае с расширением, но можно и по умолчанию указать
    расширение, и у пользователя запрашивать только имя файла"""

file_name = input("Enter file name with the extension")
print("Enter your content")

# Запись данных ввода, ограничение - пустая строка
try:
    with open(file_name, "x", encoding='utf-8') as user_input:
        user_input.write("\n".join(iter(input, "")))
except IOError:
    print("File already exists")
except EOFError:
    print("Input error")
