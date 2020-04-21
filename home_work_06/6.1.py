from time import sleep
from sys import stderr
from sys import stdout


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        pos = 1  # Индекс цветов из списка
        p = 1  # Для определения границ, меняет свой знак в строке 18
        for i in range(10):
            # print(self.__color[pos])  # Вывод по очереди в новой строке
            # stderr.write(f"{self.__color[pos]:7}\r")  # Выводит только в консоли
            # sleep(0.5)  # С задержкой
            stdout.write('\r' + self.__color[pos])  # Вывод в одной строке
            sleep(2) if self.__color[pos] == 'yellow' else sleep(7)
            p = -p if pos >= (len(self.__color) - 1) or pos <= 0 else p
            pos += p


working_tl = TrafficLight()
working_tl.running()
