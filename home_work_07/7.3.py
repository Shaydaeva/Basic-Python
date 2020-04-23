class Cell:
    def __init__(self, quan=int()):
        self.quan = quan

    def __str__(self):
        return f"{self.quan}"

    def __add__(self, other):
        return self.quan + other.quan

    def __sub__(self, other):
        if (self.quan - other.quan) > 0:
            return self.quan - other.quan
        else:
            return "Вычитание не может быть произведено"

    def __mul__(self, other):
        return self.quan * other.quan

    def __truediv__(self, other):
        if (self.quan / other.quan) < 1:
            return "Частное меньше единицы"
        else:
            return self.quan // other.quan

    def make_order(self, row):
        quantity = self.quan
        count = 0
        while quantity > row:
            print(f"{'*' * row}")
            quantity -= row
            count += 1
        else:
            print(f"{'*' * quantity}")



cell_1 = Cell(7)
cell_2 = Cell(10)

cell_3 = Cell(cell_1 + cell_2)
cell_4 = Cell(cell_1 - cell_2)
cell_5 = Cell(cell_1 * cell_2)
cell_6 = Cell(cell_1 / cell_2)
print(cell_3, cell_4, cell_5, cell_6, sep='\n')
cell_3.make_order(5)
print(cell_3)
