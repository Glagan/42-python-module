import numpy as np


class ScrapBooker:
    def __init__(self) -> None:
        pass

    def crop(self, array: np.ndarray, dimensions: tuple, position: tuple = (0, 0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
            array: numpy.ndarray
            dim: tuple of 2 integers.
            position: tuple of 2 integers.
        Returns:
            new_arr: the cropped numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(dimensions, tuple) or not isinstance(position, tuple):
            return None
        if len(dimensions) != 2 or len(position) != 2:
            return None
        if any(not isinstance(i, int) for i in dimensions) or any(not isinstance(i, int) for i in position):
            return None
        if dimensions > array.shape:
            dimensions = array.shape
        # Dimensions are reversed according to subject for some reasons...
        return array[position[0]:(position[0] + dimensions[0]), position[1]:(position[1] + dimensions[1])]

    def thin(self, array: np.ndarray, n: int, axis: int):
        """
        Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
        Args:
            array: numpy.ndarray.
            n: non null positive integer lower than the number of row/column of the array
            (depending of axis value).
            axis: positive non null integer.
        Returns:
            new_arr: thined numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(n, int) or not isinstance(axis, int):
            return None
        if n <= 0 or axis < 0 or axis > 1:
            return None
        if len(array.shape) != 2:
            return None
        # Reverse axis according to subject for some reasons...
        axis = 0 if axis else 1
        if array.shape[axis] < n:
            return None
        mask = np.full((array.shape[axis]), False)
        for i in range(n - 1, array.shape[axis], n):
            mask[i] = True
        return np.delete(array, mask, axis=axis)

    def juxtapose(self, array: np.ndarray, n: int, axis: int):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.
        Returns:
            new_arr: juxtaposed numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(n, int) or not isinstance(axis, int):
            return None
        if n <= 0 or axis < 0 or axis > 1:
            return None
        # -- **NO** inverted axis for some other reasons on this one
        carry = array
        for _ in range(1 if n == 1 else n - 1):
            carry = np.concatenate((carry, array), axis=axis)
        return carry

    def mosaic(self, array: np.ndarray, dimensions: tuple):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
            array: numpy.ndarray.
            dim: tuple of 2 integers.
        Returns:
            new_arr: mosaic numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(dimensions, tuple):
            return None
        if len(dimensions) != 2:
            return None
        if any(not isinstance(i, int) for i in dimensions):
            return None
        if any(i <= 0 for i in dimensions):
            return None
        carry = array
        if dimensions[0] > 1:
            carry = self.juxtapose(array, dimensions[0] - 1, 0)
        if dimensions[1] > 1:
            carry = self.juxtapose(carry, dimensions[1] - 1, 1)
        return carry
