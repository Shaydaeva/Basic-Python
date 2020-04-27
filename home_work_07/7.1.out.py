class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return 'Матрица\n' + '\n'.join([''.join([f"{i:>5}" for i in row]) for row in self.matrix]) + '\n'

    def __add__(self, other):
        res_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(list(self.matrix))):
            for j in range(len(list(self.matrix)[0])):
                res_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return res_matrix


my_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
my_3 = Matrix(my_1 + my_2)  # Только здесь получится красивый вывод
print(my_1)
print(my_2)
print(my_3)
my_4 = my_2 + my_3  # Здесь просто список списков получился
print(my_4)
