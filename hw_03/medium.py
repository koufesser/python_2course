import numpy as np
import numbers


class CommonClass:
    def __init__(self):
        self.value = None


class StrMixin(CommonClass):
    def __str__(self):
        str_matrix = [[str(i) for i in j] for j in self.value]
        return "".join(list(map(lambda s: ' '.join(s) + '\n', str_matrix)))


class GetMixin(CommonClass):
    def getvalue(self):
        return self.value


class FPrintMixin(CommonClass):
    def fprint(self, file):
        f = open(file, 'w')
        f.write(str(self))


class SetMixin(CommonClass):
    def setvalue(self, value):
        self.value = value


class MatrixLike(np.lib.mixins.NDArrayOperatorsMixin, StrMixin, GetMixin, FPrintMixin):
    def __init__(self, value):
        super().__init__()
        if isinstance(value, np.ndarray):
            self.value = value
        else:
            self.value = np.ndarray(value)
    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (MatrixLike,)):
                return NotImplemented

        inputs = tuple(x.value if isinstance(x, MatrixLike) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.value if isinstance(x, MatrixLike) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)


def medium():
    np.random.seed = 0
    a = MatrixLike(np.random.randint(0, 10, (10, 10)))
    b = MatrixLike(np.random.randint(0, 10, (10, 10)))
    f1 = open('artifacts/medium/matrix+.txt', 'w')
    f2 = open('artifacts/medium/matrix_mul.txt', 'w')
    f3 = open('artifacts/medium/matrix@.txt', 'w')
    c = a + b
    c.fprint()
    c = a * b
    c.fprint()
    c = a @ b
    c.fprint()


if __name__ == '__name__':
    medium()
