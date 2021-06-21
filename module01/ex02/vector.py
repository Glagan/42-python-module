class Vector:
    def __init__(self, initializer) -> None:
        self.values = []
        if type(initializer) is int:
            if initializer < 0:
                raise TypeError(
                    "You can't have a Vector with a negative size.")
            for i in range(initializer):
                self.values.append(float(i))
            self.size = initializer
        elif isinstance(initializer, tuple):
            if len(initializer) != 2 or not type(initializer[0]) is int or not type(initializer[1]) is int:
                raise TypeError(
                    'Expected a (min, max) tuple got {}.'.format(initializer))
            if initializer[0] > initializer[1]:
                raise TypeError("Min can't be bigger than max.")
            for i in range(initializer[0], initializer[1]):
                self.values.append(float(i))
            self.size = len(self.values)
        elif isinstance(initializer, list):
            for i in initializer:
                if not type(i) is float:
                    raise TypeError(
                        'Vector initializer must be an array of float, got {}.'.format(i))
            self.values = initializer[0:]
            self.size = len(self.values)
        raise TypeError(
            'Vector initializer must be a list, size or a min-max range.')

    def __add__(self, a):
        if type(a) is int or type(a) is float:
            return Vector(list(self.values[index] + a for index in range(self.size)))
        elif isinstance(a, Vector):
            if self.size != a.size:
                raise ArithmeticError(
                    "Two Vectors need the same dimension to be added.")
            return Vector(list(self.values[index] + a.values[index] for index in range(self.size)))
        return NotImplemented

    def __radd__(self, a):
        return self.__add__(a)

    def __sub__(self, a):
        if type(a) is int or type(a) is float:
            return Vector(list(self.values[index] - a for index in range(self.size)))
        elif isinstance(a, Vector):
            if self.size != a.size:
                raise ArithmeticError(
                    "Two Vectors need the same dimension to be substracted.")
            return Vector(list(self.values[index] - a.values[index] for index in range(self.size)))
        return NotImplemented

    def __rsub__(self, a):
        return self.__sub__(a)

    def __mul__(self, a):
        if type(a) is int or type(a) is float:
            return Vector(list(self.values[index] * a for index in range(self.size)))
        elif isinstance(a, Vector):
            if self.size != a.size:
                raise ArithmeticError(
                    "Two Vectors need the same dimension to be multiplicated.")
            return sum((self.values[index] * a.values[index]) for index in range(self.size))
        return NotImplemented

    def __rmul__(self, a):
        return self.__mul__(a)

    def __truediv__(self, a):
        if type(a) is int or type(a) is float:
            if int(a) == 0:
                raise ZeroDivisionError("You can't divide a Vector by 0 !")
            return Vector(list(self.values[index] / a for index in range(self.size)))
        return NotImplemented

    def __rtruediv__(self, a):
        return NotImplemented

    def __str__(self):
        return '(Vector {})'.format(str(self.values))

    def __repr__(self):
        return '<Vector of size {} {}>'.format(self.size, self.values)
