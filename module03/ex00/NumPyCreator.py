import numpy as np

valid_types = (int, float, bool, str)


class NumPyCreator:
    def check_list(self, lst: list):
        expect_list = None
        expect_length = -1
        for item in lst:
            is_list = isinstance(item, list)
            if expect_list is True and not is_list:
                return False
            elif expect_list is False and is_list:
                return False
            if is_list:
                length = len(item)
                if expect_length < 0:
                    expect_length = len(item)
                elif length != expect_length:
                    return False
                expect_list = True
                if not self.check_list(item):
                    return False
            else:
                expect_list = False
                if not type(item) in valid_types:
                    print("found invalid type of {} / {} / {}".format(type(item), item, type(item) == int))
                    return False
        return True

    def from_list(self, lst: list):
        if not isinstance(lst, list):
            return None
        if not self.check_list(lst):
            return None
        return np.array(lst)

    def from_tuple(self, tpl: tuple):
        if not isinstance(tpl, tuple):
            return None
        return np.array(tpl)

    def from_iterable(self, itr):
        lst = [i for i in itr]
        return self.from_list(lst)

    def from_shape(self, shape: tuple, value=0.0):
        if not isinstance(shape, tuple):
            return None
        return np.full(shape, value)

    def random(self, shape: tuple):
        if not isinstance(shape, tuple):
            return None
        return np.random.rand(*shape)

    def identity(self, n: int):
        if not isinstance(n, int):
            return None
        if n < 0:
            return None
        return np.identity(n)
