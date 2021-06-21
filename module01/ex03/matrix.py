class Matrix:
    def __init__(self, initializer, shape=None) -> None:
        self.data = []
        if shape == None:
            if isinstance(initializer, list):
                self.shape = None
                if not initializer:
                    raise TypeError("A Matrix can't be smaller than 1x1.")
                for col in initializer:
                    if not isinstance(col, list):
                        raise TypeError(
                            'Each columns in a row must be a list.')
                    if not self.shape:
                        if not col:
                            raise TypeError(
                                "A Matrix can't be smaller than 1x1.")
                        self.shape = (len(initializer), len(col))
                    elif self.shape[1] != len(col):
                        raise TypeError(
                            'Each columns must have the same length.')
                    self.data.append([])
                    for value in col:
                        if type(value) is not float:
                            raise TypeError(
                                'Each values in the matrix must be a float.')
                        self.data[-1].append(value)
            elif isinstance(initializer, tuple):
                if len(initializer) != 2 or not type(initializer[0]) is int or not type(initializer[1]) is int:
                    raise TypeError(
                        'Expected a (min, max) tuple as a shape got {}.'.format(initializer))
                if initializer[0] < 1 or initializer[1] < 1:
                    raise TypeError("A Matrix can't be smaller than 1x1.")
                self.data = [[0.0] * initializer[1]] * initializer[0]
                self.shape = (initializer[0], initializer[1])
            else:
                raise TypeError(
                    'Matrix initializer must be a list of list or a shape.')
        else:
            if not isinstance(initializer, list):
                raise TypeError(
                    'Matrix initializer must be a list of list of the given shape')
            if not isinstance(shape, tuple) or len(shape) != 2 or not type(shape[0]) is int or not type(shape[1]) is int:
                raise TypeError(
                    'Expected a (min, max) tuple as a shape got {}.'.format(initializer))
            if shape[0] < 1 or shape[1] < 1:
                raise TypeError("A Matrix can't be smaller than 1x1.")
            self.shape = (shape[0], shape[1])
            self.data = []
            if len(initializer) != shape[0]:
                raise TypeError('Invalid list for given shape.')
            for col in initializer:
                if not isinstance(col, list):
                    raise TypeError(
                        'Each columns in a row must be a list.')
                if self.shape[1] != len(col):
                    raise TypeError(
                        'Invalid column length for given shape.')
                self.data.append([])
                for value in col:
                    if type(value) is not float:
                        raise TypeError(
                            'Each values in the matrix must be a float.')
                    self.data[-1].append(value)

    def __add__(self, a):
        if type(a) is int or type(a) is float:
            result = []
            for row in self.data:
                result.append(list(col + a for col in row))
            return Matrix(result, self.shape)
        elif isinstance(a, Matrix):
            if self.shape != a.shape:
                raise TypeError('You can only add Matrices of the same size.')
            result = []
            for row in range(self.shape[0]):
                result.append(
                    list(self.data[row][col] + a.data[row][col] for col in range(self.shape[1])))
            return Matrix(result, self.shape)
        return NotImplemented

    def __radd__(self, a):
        if type(a) is int or type(a) is float:
            return self.__add__(a)
        return NotImplemented

    def __sub__(self, a):
        if type(a) is int or type(a) is float:
            result = []
            for row in self.data:
                result.append(list(col - a for col in row))
            return Matrix(result, self.shape)
        elif isinstance(a, Matrix):
            if self.shape != a.shape:
                raise TypeError(
                    'You can only substract Matrices of the same size.')
            result = []
            for row in range(self.shape[0]):
                result.append(
                    list(self.data[row][col] + a.data[row][col] for col in range(self.shape[1])))
            return Matrix(result, self.shape)
        return NotImplemented

    def __rsub__(self, a):
        if type(a) is int or type(a) is float:
            return self.__sub__(a)
        return NotImplemented

    def __truediv__(self, a):
        if type(a) is int or type(a) is float:
            if int(a) == 0:
                raise ZeroDivisionError("You can't divide a Matrix by 0 !")
            result = []
            for row in self.data:
                result.append(list(col / a for col in row))
            return Matrix(result, self.shape)
        return NotImplemented

    def __rtruediv__(self, a):
        return NotImplemented

    def __mul__(self, a):
        if isinstance(a, Matrix):
            # m*n n*1 -> m*1
            if self.shape[1] == a.shape[0] and a.shape[1] == 1:
                result = []
                for row in self.data:
                    new_row = 0
                    for index in range(self.shape[1]):
                        new_row += (row[index] * a.data[index][0])
                    result.append([new_row])
                return Matrix(result, (self.shape[0], 1))
            # m*n n*p -> m*p
            elif self.shape[1] == a.shape[0]:
                result = []
                for row in range(self.shape[0]):
                    current_row = []
                    for index in range(a.shape[1]):
                        row_result = 0
                        for j in range(self.shape[1]):
                            row_result += (
                                self.data[row][j] * a.data[j][index])
                        current_row.append(row_result)
                    result.append(current_row)
                return Matrix(result, (self.shape[0], a.shape[1]))
            raise TypeError(
                "You can only multiply a Matrix with the same shape or a vector that match the rows.")
        elif type(a) is int or type(a) is float:
            result = []
            for row in self.data:
                result.append(list(col * a for col in row))
            return Matrix(result, self.shape)
        return NotImplemented

    def __rmul__(self, a):
        if type(a) is int or type(a) is float:
            return self.__mul__(a)
        return NotImplemented

    def __str__(self):
        return '(Matrix {})'.format(str(self.data))

    def __repr__(self):
        return '<Matrix of shape {} {}>'.format(self.shape, self.data)
