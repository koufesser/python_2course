import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.height = len(matrix)
        self.length = len(matrix[0])
        for i in range(self.height):
            if len(matrix[i]) != self.length:
                raise ValueError

    def __add__(self, other):
        if self.length != other.length or self.height != other.height:
            return 1
        new_matrix = [[0 for j in range(self.length)] for i in range(self.height)]
        for i in range(self.length):
            for j in range(self.height):
                new_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(new_matrix)

    def __matmul__(self, other):
        if self.length != other.length or self.height != other.height:
            return 1
        new_matrix = [[0 for j in range(self.length)] for i in range(self.height)]
        for i in range(self.length):
            for j in range(self.height):
                new_matrix[i][j] = self.matrix[i][j] * other.matrix[i][j]
        return Matrix(new_matrix)

    def __mul__(self, other):
        if self.length != other.height:
            return 1
        new_matrix = [[0 for j in range(other.length)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(other.length):
                new_matrix[i][j] = 0
                for k in range(self.length):
                    new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(new_matrix)

    def __str__(self):
        str_matrix = [[str(i) for i in j] for j in self.matrix]
        return "".join(list(map(lambda s: ' '.join(s) + '\n', str_matrix)))


def easy():
    np.random.seed = 0
    ta = np.random.randint(0, 10, (10, 10))
    tb = np.random.randint(0, 10, (10, 10))
    a = Matrix(ta)
    b = Matrix(tb)
    f1 = open('artifacts/easy/matrix+.txt', 'w')
    f2 = open('artifacts/easy/matrix_mul.txt', 'w')
    f3 = open('artifacts/easy/matrix@.txt', 'w')
    f1.write(str(a + b))
    f2.write(str(a * b))
    f3.write(str(a @ b))
    f1.close()
    f2.close()
    f3.close()


if __name__ == '__main__':
    easy()
