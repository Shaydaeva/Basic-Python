class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Рисование ручкой. Взят предмет {self.title}")


class Pencil(Stationery):
    def draw(self):
        print("Рисование карандашом")


class Handle(Stationery):
    def draw(self):
        print("Рисование маркером")


first_pen = Pen('Красная ручка')
first_pen.draw()

pencil_1 = Pencil('Обычный карандаш')
pencil_1.draw()

handle_1 = Handle('Маркер для выделения')
handle_1.draw()

stationery_1 = Stationery('Что-то новенькое')
stationery_1.draw()
