import numpy as np


class ScrapBooker:
    def crop(self, array: np.ndarray, dimensions: tuple, position: tuple = (0, 0)):
        if dimensions > array.shape:
            dimensions = array.shape
        return array[position[0]:(position[0] + dimensions[0]), position[1]:(position[1] + dimensions[1])]

    def thin(self, array: np.ndarray, n: int, axis: int):
        # Reverse axis according to subject for some reasons...
        axis = 0 if axis else 1
        mask = np.full((array.shape[axis]), True)
        for i in range(0, array.shape[axis], n):
            mask[i] = False
        return np.delete(array, mask, axis=axis)

    def juxtapose(self, array: np.ndarray, n: int, axis: int):
        # Reverse axis according to subject for some reasons...
        axis = 0 if axis else 1
        carry = array
        for i in range(n):
            if axis == 0:
                carry = np.vstack((carry, array))
            else:
                carry = np.hstack((carry, array))
        return carry

    def mosaic(self, array: np.ndarray, dimensions: tuple):
        carry = array
        if dimensions[0] > 1:
            carry = self.juxtapose(array, dimensions[0] - 1, 1)
        if dimensions[1] > 1:
            carry = self.juxtapose(carry, dimensions[1] - 1, 0)
        return carry
