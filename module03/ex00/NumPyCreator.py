import numpy as np


class NumPyCreator:
    def type_from_container(self, container):
        if not len(container):
            return np.float64
        if isinstance(container[0], list) or isinstance(container[0], tuple):
            return self.type_from_container(container[0])
        return type(container[0])

    def from_list(self, lst: list, dtype=None):
        if not dtype:
            dtype = self.type_from_container(lst)
        return np.array(lst, dtype=dtype)

    def from_tuple(self, tpl: tuple, dtype=None):
        if not dtype:
            dtype = self.type_from_container(tpl)
        return np.array(tpl, dtype=dtype)

    def from_iterable(self, itr, dtype=None):
        lst = list(i for i in itr)
        if not dtype:
            dtype = self.type_from_container(lst)
        return np.array(lst, dtype=dtype)

    def from_shape(self, shape: tuple, value=None, dtype=None):
        if value == None:
            value = 0.0
        if not dtype:
            dtype = type(value)
        return np.full(shape, value, dtype=dtype)

    def random(self, shape: tuple, dtype=np.float64):
        rng = np.random.default_rng(0)
        return rng.random(shape, dtype=dtype)

    def identity(self, n: int, dtype=np.float64):
        return np.identity(n, dtype=dtype)
