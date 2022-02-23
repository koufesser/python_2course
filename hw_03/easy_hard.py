import numpy as np
from functools import reduce


class CommonClass:
    def __init__(self):
        self.matrix = None
        self.height = None
        self.length = None


class HashMixin(CommonClass):
    def __hash__(self):
        matrix = [i for j in self.matrix for i in j]
        return int(reduce(lambda x, y: x + y * y, matrix))


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


class HashableMatrix(Matrix, HashMixin):
    dict = dict()

    def __init__(self, m):
        super().__init__(m)

    def __mul__(self, other):
        h1 = hash(self)
        h2 = hash(other)
        if (h1, h2) in HashableMatrix.dict:
            return dict[(h1, h2)]
        else:
            mul = super(HashableMatrix, self).__mul__(other)
            self.dict[(h1, h2)] = mul
            return mul

    def __ne__(self, other):
        if self.length != other.length or self.height != other.height:
            return True
        for i in range(self.height):
            for j in range(self.length):
                if (self.matrix[i][j] != other.matrix[i][j]):
                    return True
        return False

    def clearhash(self):
        HashableMatrix.dict.clear()

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


def hard():
    while True:
        a = HashableMatrix(np.random.randint(0, 5, (3, 3)))
        b = HashableMatrix(np.random.randint(0, 5, (3, 3)))
        c = HashableMatrix(np.random.randint(0, 5, (3, 3)))
        d = b
        ab = a @ b
        a.clearhash()
        cd = c @ d
        if hash(a) == hash(c) and a != c and ab != cd:
            with open('artifacts/hard/A.txt', 'w') as f:
                f.write(str(a))
            with open('artifacts/hard/B.txt', 'w') as f:
                f.write(str(b))
            with open('artifacts/hard/C.txt', 'w') as f:
                f.write(str(c))
            with open('artifacts/hard/D.txt', 'w') as f:
                f.write(str(d))
            with open('artifacts/hard/AB.txt', 'w') as f:
                f.write(str(ab))
            with open('artifacts/hard/CD.txt', 'w') as f:
                f.write(str(cd))
            with open('artifacts/hard/hash.txt', 'w') as f:
                f.write(f"hash(AB) = {hash(ab)}, hash(CD) = {hash(cd)}")
            break

if __name__ == '__main__':
    easy()
    hard()
