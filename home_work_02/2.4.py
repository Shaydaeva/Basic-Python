user_str = input('Введите строку из нескольких слов, разделенных пробелами: ').split()

for ind, i in enumerate(user_str, 1):
    print(ind, i[:10])
