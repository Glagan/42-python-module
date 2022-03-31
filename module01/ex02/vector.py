class Vector:
    def __init__(self, initializer) -> None:
        """
        Create a new 1D or 2D Vector from a given size, range or other Vector.
        - shape has the format (rows, columns)
        """
        self.values = []
        # Basic size column Vctor
        if isinstance(initializer, int):
            if initializer < 0:
                raise TypeError(
                    "You can't have a Vector with a negative size.")
            for i in range(initializer):
                self.values.append([float(i)])
            self.shape = (initializer, 1 if initializer > 0 else 0)
        elif isinstance(initializer, tuple):
            if len(initializer) != 2 or not isinstance(initializer[0], int) or not isinstance(initializer[1], int):
                raise TypeError(
                    'Expected a (min, max) tuple got {}.'.format(initializer))
            if initializer[0] > initializer[1]:
                raise TypeError("Min can't be bigger than max.")
            for i in range(initializer[0], initializer[1]):
                self.values.append([float(i)])
            length = len(self.values)
            self.shape = (length, 1 if length > 0 else 0)
        elif isinstance(initializer, list):
            is_1d = Vector.validate_list(initializer)
            self.values = initializer[0:]
            d_length = len(self.values)
            if is_1d:
                self.shape = (1 if d_length > 0 else 0, d_length)
            else:
                d2_length = len(self.values[0]) if d_length > 0 else 0
                self.shape = (d_length if d2_length > 0 else 0, len(self.values[0]) if d_length > 0 else 0)
        else:
            raise TypeError('Vector initializer must be a list, size or a min-max range.')

    def is_column_vector(self) -> bool:
        return len(self.values) > 0 and isinstance(self.values[0], list)

    def is_row_vector(self) -> bool:
        return not self.is_column_vector()

    def dot(self, b):
        if isinstance(b, Vector):
            if self.shape != b.shape:
                raise ArithmeticError(
                    "Two Vectors need the same dimension to be produce a dot product.")
            # Handle zero vector
            if self.shape == (0, 0):
                return 0.0
            # Flatten and add the lists
            vector_sum = 0.0
            if self.is_column_vector():
                vector_sum = sum([a[0] * b[0] for (a, b) in zip(self.values, b.values)])
            else:
                vector_sum = sum([a * b for (a, b) in zip(self.values, b.values)])
            return vector_sum
        return NotImplemented

    def T(self):
        # Handle zero vector
        if self.shape == (0, 0):
            if self.is_column_vector():
                return Vector([])
            return Vector([[]])
        # Transpose each columns <-> rows
        if self.is_column_vector():
            return Vector([v[0] for v in self.values])
        return Vector([[v] for v in self.values])

    def validate_list(number_list: list, columns=0, allow_nested_list=True) -> bool:
        """
        Validate a list of float or nested list of floats against all errors.
        The number_list should strictly be a list of float,
        or a list of list float with the exact same length.
        """
        has_one_float = not allow_nested_list or len(number_list) == 0
        has_one_list = False
        has_empty_row = False
        for i in number_list:
            is_float = isinstance(i, float)
            is_list = isinstance(i, list)
            if has_empty_row:
                raise TypeError('A zero Vector can only have a single row/column')
            if (has_one_list and is_float) or (has_one_float and not is_float) or (is_list and not allow_nested_list):
                raise TypeError('Vector initializer must be an array of float or a nested array of float, got {}.'.format(i))
            if is_list:
                current_length = len(i)
                if current_length > 1:
                    raise TypeError('Only single column Vectors are supported.')
                elif current_length == 0:
                    has_empty_row = True
                has_one_list = True
                Vector.validate_list(i, False)
            else:
                has_one_float = True
        return has_one_float

    def __add__(self, b):
        if isinstance(b, int) or isinstance(b, float):
            if self.is_column_vector():
                return Vector([[v[0] + b] for v in self.values])
            return Vector([v + b for v in self.values])
        elif isinstance(b, Vector):
            if self.shape != b.shape:
                raise ArithmeticError("Two Vectors need the same dimension to be added.")
            if self.is_column_vector():
                return Vector([[a[0] + b[0]] for (a, b) in zip(self.values, b.values)])
            return Vector([a + b for (a, b) in zip(self.values, b.values)])
        return NotImplemented

    def __radd__(self, b):
        return self.__add__(b)

    def __sub__(self, b):
        if isinstance(b, int) or isinstance(b, float):
            if self.is_column_vector():
                return Vector([[v[0] - b] for v in self.values])
            return Vector([v - b for v in self.values])
        elif isinstance(b, Vector):
            if self.shape != b.shape:
                raise ArithmeticError("Two Vectors need the same dimension to be substracted.")
            if self.is_column_vector():
                return Vector([[a[0] - b[0]] for (a, b) in zip(self.values, b.values)])
            return Vector([a - b for (a, b) in zip(self.values, b.values)])
        return NotImplemented

    def __rsub__(self, b):
        return self.__sub__(b)

    def __mul__(self, b):
        if isinstance(b, int) or isinstance(b, float):
            if self.is_column_vector():
                return Vector([[v[0] * b] for v in self.values])
            return Vector([v * b for v in self.values])
        elif isinstance(b, Vector):
            if self.shape != b.shape:
                raise ArithmeticError("Two Vectors need the same dimension to be multiplicated.")
            if self.is_column_vector():
                return Vector([[a[0] * b[0]] for (a, b) in zip(self.values, b.values)])
            return Vector([a * b for (a, b) in zip(self.values, b.values)])
        return NotImplemented

    def __rmul__(self, b):
        return self.__mul__(b)

    def __truediv__(self, b):
        if isinstance(b, int) or isinstance(b, float):
            if b == 0:
                raise ZeroDivisionError("You can't divide b Vector by 0 !")
            if self.is_column_vector():
                return Vector([[v[0] / b] for v in self.values])
            return Vector([v / b for v in self.values])
        return NotImplemented

    def __rtruediv__(self, b):
        return NotImplemented

    def __str__(self):
        return '(Vector {})'.format(str(self.values))

    def __repr__(self):
        return '<Vector of size {} {}>'.format(self.shape, self.values)
