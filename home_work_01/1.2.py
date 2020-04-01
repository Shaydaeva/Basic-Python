seconds = int(input('Введите время в секундах: '))

hour = seconds//3600
minute = (seconds - hour * 3600) // 60
sec = seconds - hour * 3600 - minute * 60

print(f"{hour:02}:{minute:02}:{sec:02}")
