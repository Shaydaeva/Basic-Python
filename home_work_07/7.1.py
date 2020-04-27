class Matrix:
    """Работает с равноразмерными матрицами"""
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return 'Матрица\n' + '\n'.join([''.join([f"{i:>5}" for i in row]) for row in self.matrix]) + '\n'

    def __add__(self, other):
        new_matrix = []
        for el in range(len(list(self.matrix))):
            new_list = []
            for i, j in zip(self.matrix[el], other.matrix[el]):
                new_list.append(i + j)
            new_matrix.append(new_list)
        #  Вывод прописала еще раз, чтобы в случае my_3 = my_1 + my_2 тоже получался красивый вывод
        return 'Сумма матриц:\n' + '\n'.join([''.join([f"{i:>5}" for i in row]) for row in new_matrix])



my_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(my_1)
print(my_2)
my_3 = my_1 + my_2
print(my_3)
