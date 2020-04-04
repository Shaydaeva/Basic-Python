user_var = int(input("Введите целое положительное число: "))

max_num = 0

while user_var != 0:
    num = user_var % 10
    if num == 9:
        max_num = num
        break
    elif num > max_num:
        max_num = num
    user_var = user_var // 10

print(f"Самая большая цифра в числе - {max_num}")
